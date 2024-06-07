from googletrans import Translator
from deep_translator import GoogleTranslator


def translator(text, lang_code):
    translator = Translator()
    translated_text = translator.translate(text, dest=lang_code).text
    return translated_text


def deep_translator(text, source, lang_code):
    deep_translator = GoogleTranslator(source=source, target=lang_code)
    translated_text = deep_translator.translate(text)
    return translated_text
