import os

import replicate

from utils.translator import translator, deep_translator

os.environ["REPLICATE_API_TOKEN"] = "r8_46epRPIxt52foXXpAnwWwiZ81gkkmiT223AIP"


def meta_ai(prompt):
    outputs = []
    input = {
        "prompt": prompt

    }

    for event in replicate.stream(
            "meta/meta-llama-3-8b",
            input=input):
        outputs.append(str(event))
        print(''.join(outputs))
    return deep_translator(''.join(outputs), 'en', 'ru')



