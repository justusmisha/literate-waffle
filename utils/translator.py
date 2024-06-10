from deep_translator import GoogleTranslator


def deep_translator(text, source, lang_code):
    deep_translator = GoogleTranslator(source=source, target=lang_code)
    translated_text = deep_translator.translate(text)
    return translated_text
