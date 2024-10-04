import requests


def posting_post_wp(title, content, image_id, header, url):
    post = {
        'title': title,
        'status': 'publish',
        'content': content,
        'featured_media': str(image_id),
    }

    response = requests.post(f'{url}posts', headers=header, json=post)
    print(response.json())
    if response.status_code == 201:
        print('Все ок')
    else:
        print(response.status_code)


def posting_media_wp(file_path, wp_media_url, header):
    # вылаживаем фотку в медиафайлы и берем ее ссылку
    media = {
        'file': open(file_path, "rb"),
    }

    response = requests.post(fr'{wp_media_url}media', headers=header, files=media).json()

    return response['id']


def update_media_wp(header, url, title, id_media):
    # обновляем данные у медиа
    update_image = {
        'alt_text': title,
        'caption': title,
        'description': title,
    }
    updated_image_json = requests.post(url + 'media/' + str(id_media), headers=header, json=update_image).json()

    return updated_image_json



