def postint_post_tg(id_channel, content, bot):
    bot.send_message(id_channel,
                     content,
                     parse_mode='html')


def posting_media_tg(id_channel, folder_media, news_title, bot):
    photo = open(folder_media, 'rb')
    bot.send_photo(id_channel,
                   photo,
                   caption=news_title)
