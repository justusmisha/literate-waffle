import os

import replicate

from utils.functions import text_formating
from utils.translator import deep_translator

os.environ["REPLICATE_API_TOKEN"] = "r8_5Bbm0UJC7hhMBsCwroy0GIAICO0xs3Z1uJKh6"


def meta_ai(prompt):
    input = {
        "prompt": prompt,
        'max_new_tokens': 265,
        'length_penalty': 0.5

    }

    output = replicate.run(
            "meta/meta-llama-3-8b",
            input=input)
    return deep_translator(text_formating(''.join(output), '**'), 'en', 'ru')



