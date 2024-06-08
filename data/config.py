import os

BOT_TOKEN = "6595975751:AAF2bkyuFbPhdu8243DtsGpkFkkk2JyvS80"

categories = ["Личные вещи", "Транспорт", "Недвижимость", "Работа", "Услуги", "Для дома и дачи", "Бытовая электроника",
              "Хобби и отдых", "Животные", "Для бизнеса"]


# prompt_common = ("Создайте привлекательное описание объявления, адаптированное к Avito для данной категории. Укажите "
#                  "ключевые моменты продажи и информацию, предоставленную пользователем. Убедитесь, что объявление "
#                  "лаконичное, привлекательное и оптимизировано для привлечения потенциального покупателя. "
#                  "Используйте смайлики, но не слишком много. Убедитесь что оно максимально креативное и продающее. Не "
#                  "присылай вступление по типу 'Вот пример объявления' и не присылай заключение. Категория: "
#                  "category. Ключевые слова пользователя: key_words.")


prompt_common_en_1 = "###Instructions:\nYou are a copywriter and write selling ads for avito about "

prompt_common_en_2 = " now you need to write a text for a locational ad for category "

prompt_common_en_3 = ", keep in mind that the ad should have such a structure: a short title, tell about the "

prompt_common_en_4 = (". Then make call to  write to avito or make phone call, then the benefits and completion too "
                      "with a "
                      "request to save the ad to favorites. Use emojis to increase the readability of "
                      "the text. Don't use such symbols as * and \". Be sure that all your suggestions and thoughts "
                      "come to a logical end.\n###Response:")
