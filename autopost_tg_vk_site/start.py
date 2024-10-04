# -*- coding: utf-8 -*-
import time
import json
import base64
import telebot

from sheet import update_sheet, read_sheet

from gpt import gpt
from getimg import create_photo
from yandexart import create_yandex_photo

from content_fix import fix_text

from wordpress import posting_post_wp, posting_media_wp, update_media_wp
from telegram import posting_media_tg, postint_post_tg
from vk import posting_media_vk, posting_post_vk


def start(event, context):
    print('start function2')
    how_many_to_post = 1  # постим только 1 пост

    # выбираем getimg - 1 / yandexart - 2
    photo_ai = 2

    # куда вылаживать
    site = 'yes'  # сайт
    tg = 'yes'  # телеграм группa
    vk = 'yes'  # вк сообщество
    google_sheets = 'yes'  # google таблицы

    # апи ключи
    api_gpt = "API KEY GPT"
    api_getimg = 'API KEY GETIMG'
    api_key_bot_tg = 'API kEY TG'
    api_key_vk = 'vk1.a.api_key_vk'
    api_key_yndx = 'api_key_vk'

    # данные wordpress
    url_wp = 'https://your_site/wp-json/wp/v2/'
    user = 'admin'
    password = 'qqqq qqqq qqqq qqqq qqqq qqqq'

    # данные telegram
    bot = telebot.TeleBot(api_key_bot_tg)
    id_channel = '@chanel_tg'  # канал в тг

    # данные вк
    url_server_vk = 'upload_server_vk'

    # данные google sheets
    name_sheet_read = 'python_sheet'  # для чтения
    name_sheet_write = 'sheet_write'  # для записи данных

    # путь к фотке
    file_path = r"/function/storage/bucket"
    file_media = file_path + '/photo.jpeg'

    # текст для промежуточного гпт
    intermediate_system_prompt = 'You are a technology blogger, create a social media post based on the news provided to output JSON. You have to give title, content, hashtags. Hashtags must be with a # sign. and as a string rather than a list. Example: "#apple #music #it"'
    intermediate_user_prompt = 'Попробуй разнообразить эти данные, перевести на русский, преобразовать в json и убрать ошибки {}'

    # фотки
    forimg_system_prompt = 'You are a technology blogger. You have to create a prompt to further generate the image to output JSON. You have to give only description for photo. Example: "description": "something"'  # для фоток
    forimg_user_prompt = 'Сделай выжимку и напиши маленький промпт(выдай в формате json и в ключе description, МНЕ НУЖЕН ТОЛЬКО JSON) для создания картинки исходя из данных по этой теме: {}'  # для фоток

    # берем данные с google sheets
    data_for_prompt = read_sheet(file_path, name_sheet_read)

    with open(file_path + '/news_visited.txt', 'r') as file_news:
        visited_news = [i.strip() for i in file_news.readlines()]

    # готовим header для wordpress
    creds = user + ':' + password
    token = base64.b64encode(creds.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}

    have_visited = 0
    for data in data_for_prompt:
        if data not in visited_news and have_visited < how_many_to_post:
            with open(file_path + '/news_visited.txt', 'a') as file_news_append:
                file_news_append.write(data + '\n')

            response_gpt_json = gpt('. '.join(data), api_gpt, intermediate_system_prompt,
                                        intermediate_user_prompt).replace('\n', '')

            data_dict = json.loads(response_gpt_json)

            title_post = data_dict['title']
            text = data_dict['content']
            hashtags = data_dict['hashtags']

            # генерируем промпт для фотки
            generate_image_prompt = gpt(data, api_gpt, forimg_system_prompt, forimg_user_prompt)
            json_response_photo = json.loads(generate_image_prompt)
            print(json_response_photo)
            json_response_photo = json_response_photo['description']

            # создаем фотку
            if photo_ai == 1:
                create_photo(api_getimg, json_response_photo, file_media)
            elif photo_ai == 2:
                create_yandex_photo(json_response_photo, file_media, api_key_yndx)

            # редакция текса(добавление запретных сайтов)
            content = fix_text(text, hashtags)

            if google_sheets == 'yes':
                update_sheet(title_post, text, hashtags, data, file_path, name_sheet_write)

            if tg == 'yes':
                posting_media_tg(id_channel, file_media, title_post, bot)
                postint_post_tg(id_channel, content, bot)

            if site == 'yes':
                id_media = posting_media_wp(file_media, url_wp, header)
                time.sleep(2)
                update_media_wp(header, url_wp, title_post, id_media)
                time.sleep(1)
                posting_post_wp(title_post, content, id_media, header, url_wp)

            if vk == 'yes':
                owner_id, media_id = posting_media_vk(file_media, api_key_vk, url_server_vk)
                posting_post_vk(content, title_post, api_key_vk, owner_id, media_id)

            have_visited += 1
            time.sleep(5)

    return {
        'statusCode': 200,
        'body': f'Функция была выполнена успешно',
    }

