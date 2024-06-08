import os

import replicate

from utils.translator import translator, deep_translator

os.environ["REPLICATE_API_TOKEN"] = "r8_EzQZBybms6Ym79NlaXVaTD5ZrG4e05900iRqi"


def meta_ai(prompt):
    outputs = []
    input = {
        "prompt": prompt

    }

    for event in replicate.stream(
            "meta/meta-llama-3-8b",
            input=input):
        outputs.append(str(event))
    return deep_translator(''.join(outputs), 'en', 'ru')



