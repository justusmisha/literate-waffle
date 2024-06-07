import os

BOT_TOKEN = "6595975751:AAF2bkyuFbPhdu8243DtsGpkFkkk2JyvS80"

categories = ["Личные вещи", "Транспорт", "Недвижимость", "Работа", "Услуги", "Для дома и дачи", "Бытовая электроника",
              "Хобби и отдых", "Животные", "Для бизнеса"]


prompt_common = ("Создайте привлекательное описание объявления, адаптированное к Avito для данной категории. Укажите "
                 "ключевые моменты продажи и информацию, предоставленную пользователем. Убедитесь, что объявление "
                 "лаконичное, привлекательное и оптимизировано для привлечения потенциального покупателя. "
                 "Используйте смайлики, но не слишком много. Убедитесь что оно максимально креативное и продающее. Не "
                 "присылай вступление по типу 'Вот пример объявления' и не присылай заключение. Категория: "
                 "category. Ключевые слова пользователя: key_words.")


prompt_common_en_1 = "You are a copywriter and write selling ads for avito in category "

prompt_common_en_2 = ", now you need to write a text for a locational ad for category "

prompt_common_en_3 = (", keep in mind that the ad should have such a structure: a short title, duplicate the title in "
                      "the text, tell about the")

prompt_common_en_4 = (", a call to action (just write to avito or call), then the benefits and completion too with a "
                      "call to save the ad to favorites and a call to call. Use emojis to increase the readability of "
                      "the text, but dont use too much of them.")
