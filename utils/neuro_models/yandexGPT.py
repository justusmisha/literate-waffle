import requests
import json


async def yandexGPT(prompt):
    prompt = {
        "modelUri": "gpt://b1gckhase84lsj8tnur5/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000",
            'minTokens': '500'
        },
        "messages": [
            {
                "role": "system",
                "text": prompt
            },

        ]
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN2AUOMm-n8cPEqq9HiTlf_Jy-lU-xXdqLUpTS"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = json.loads(response.text)['result']['alternatives'][0]['message']['text']
    return result