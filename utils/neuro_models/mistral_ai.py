import os
import replicate
from utils.functions import text_formating
from utils.translator import deep_translator

os.environ["REPLICATE_API_TOKEN"] = "r8_EzQZBybms6Ym79NlaXVaTD5ZrG4e05900iRqi"


def mistralai(prompt):
    output = replicate.run(
            "mistralai/mistral-7b-instruct-v0.2",
            input={
                "top_k": 300,
                "top_p": 0.9,
                "prompt": prompt,
                "temperature": 1,
                "max_new_tokens": 300,
                "prompt_template": "###Instructions: ",
                "presence_penalty": 0,
                "frequency_penalty": 1
            }
        )
    return deep_translator(text_formating(''.join(output), '###Response:'), 'en', "ru")


