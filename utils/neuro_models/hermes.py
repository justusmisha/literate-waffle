import os
import replicate
from utils.functions import text_formating
from utils.translator import translator

os.environ["REPLICATE_API_TOKEN"] = "r8_46epRPIxt52foXXpAnwWwiZ81gkkmiT223AIP"


def hermes(prompt):
    output = replicate.run(
        "tm-illumi/hermes:1485a4575a4cd3622d0575c5988bb60c5780768a3f6299ce5d95b6cb2ab95ba3",
        input={
            "n": 1,
            "top_p": 1,
            "max_length": 500,
            "temperature": 0.75,
            "repetition_penalty": 1,
            "prompt": "Enter roleplay mode. You're a seller at a used goods resale site. Do you want to write an ad" + prompt
        }
    )

    keyword = ['Response:', '###Response:', 'Response', '###Response']
    return translator(text_formating(''.join(output), keyword), "ru")
