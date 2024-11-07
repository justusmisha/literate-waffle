import uuid

import requests
import json


async def yandexGPT(prompt):
    session_id = str(uuid.uuid4())
    prompt = {
        "modelUri": "gpt://b1gckhase84lsj8tnur5/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "700",
            'minTokens': '500'
        },
        "messages": [
            {
                "role": "system",
                "text": prompt
            },

        ],
        "sessionId": session_id
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN2AUOMm-n8cPEqq9HiTlf_Jy-lU-xXdqLUpTS",
        "x-folder-id": "b1gi45iplkdieuk7imj9"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = json.loads(response.text)['result']['alternatives'][0]['message']['text']
    return result
