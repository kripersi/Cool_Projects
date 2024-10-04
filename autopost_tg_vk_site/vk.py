import requests


def posting_media_vk(folder_image, token, url_serv_media):
    file = {
        'file1': open(folder_image, 'rb')
    }

    media = requests.post(url_serv_media, files=file).json()  # загружаем на сервер

    result = requests.get('https://api.vk.com/method/photos.save', params={
        'access_token': token,
        'album_id': media['aid'],
        'group_id': media['gid'],
        'server': media['server'],
        'photos_list': media['photos_list'],
        'hash': media['hash'],
        'v': '5.199'
    }).json()  # загружаем в альбом

    owner_id = result['response'][0]['owner_id']
    media_id = int(result['response'][0]['id'])

    return owner_id, media_id


def posting_post_vk(content, title_post, token, owner_id, media_id):
    attachments = f'photo{owner_id}_{media_id}'

    result = requests.get('https://api.vk.com/method/wall.post', params={
        'access_token': token,
        'owner_id': owner_id,
        'from_group': '1',  # от группы
        'attachments': attachments,
        'message': f'{title_post}\n{content}',
        'v': '5.199'
    }).json()

    print(result)
