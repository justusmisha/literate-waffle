import os

import replicate

from utils.functions import text_formating
from utils.translator import deep_translator

os.environ["REPLICATE_API_TOKEN"] = "r8_JSzuYNYvHQNHrD1Mtxt0Bso2Yc545Zr1dxXis"


def meta_ai(prompt):
    input = {
        "prompt": prompt,
        'max_new_tokens': 255,
        'length_penalty': 1.0

    }

    output = replicate.run(
            "meta/meta-llama-3-8b",
            input=input)
    return deep_translator(text_formating(''.join(output), '**'), 'en', 'ru')



