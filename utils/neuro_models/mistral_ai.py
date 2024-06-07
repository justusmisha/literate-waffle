import os
import replicate

from utils.functions import text_formating
from utils.translator import translator

os.environ["REPLICATE_API_TOKEN"] = "r8_46epRPIxt52foXXpAnwWwiZ81gkkmiT223AIP"


def mistralai(prompt):
    output = replicate.run(
            "mistralai/mistral-7b-instruct-v0.2",
            input={
                "top_k": 500,
                "top_p": 0.9,
                "prompt": prompt,
                "temperature": 1,
                "max_new_tokens": 200,
                "prompt_template": "",
                "presence_penalty": 0,
                "frequency_penalty": 0.8
            }
        )
    print(text_formating(''.join(output), '###Response:'))
    return translator(text_formating(''.join(output), '###Response:'), "ru")


