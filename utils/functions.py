from data.config import *


def prompt_maker(prompt, category, key_words):
    prompt = prompt.split()

    prompt[-5] = f"{category}."
    prompt[-1] = f"{key_words}."

    return ' '.join(prompt)


def prompt_maker_en(title_form_user, base_category, key_words):
    return (prompt_common_en_1 +
            title_form_user + prompt_common_en_2 +
            base_category + prompt_common_en_3 +
            key_words + prompt_common_en_4)


def text_formating(text, keyword):
    text_spit = text.split(' ')
    for word in text_spit:
        if word in keyword:
            keyword = word
    index = text.find(keyword)

    if index != -1:
        result = text[index:]
        return result
