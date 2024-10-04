import requests
import base64
import time


def create_yandex_photo(prompt, folder, api_key_undx):
    prompt = {
        "modelUri": "art://backet_id/yandex-art/latest",
        "generationOptions": {
            "seed": "1863",
            "aspectRatio": {
                "widthRatio": "2",
                "heightRatio": "1"
            }
        },
        "messages": [
            {
                "weight": "1",
                "text": prompt,
            }
        ]
    }

    headers = {
        'Authorization': f'Api-key {api_key_undx}',
        "Content-Type": "application/json",
    }

    create_request = requests.post('https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync',
                                   headers=headers, json=prompt)
    time.sleep(10)
    for i in range(3):
        done_request = requests.get(f'https://llm.api.cloud.yandex.net:443/operations/{create_request.json()["id"]}',
                                    headers=headers)
        if done_request.json()['done']:
            with open(folder, 'wb') as file:
                file.write(base64.b64decode(done_request.json()['response']['image']))

            break
        time.sleep(5)

    return create_request.json()['id'] + '.jpeg'
