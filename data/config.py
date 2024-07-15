import os

BOT_TOKEN = "7065723843:AAHXBepc8GhvwESIsJBVoxesLJ3yOS_R3ak"

# categories = ["Личные вещи", "Транспорт", "Недвижимость", "Работа", "Услуги", "Для дома и дачи", "Бытовая электроника",
#               "Хобби и отдых", "Животные", "Для бизнеса"]

categories = ["Личные вещи", "Услуги", "Для дома и дачи", "Бытовая электроника", "Генератор ключевых слов"]


prompt_common_en_1 = "###Instructions:\nYou are a copywriter and write selling ads for avito about "

prompt_common_en_2 = " now you need to write a text for a locational ad for category "

prompt_common_en_3 = ", keep in mind that the ad should have such a structure: a short title, tell about the "

prompt_common_en_4 = (". Then make call to  write to avito or make phone call, then the benefits and completion too "
                      "with a "
                      "request to save the ad to favorites. Use emojis to increase the readability of "
                      "the text. Don't use such symbols as * and \". Be sure that all your suggestions and thoughts "
                      "come to a logical end.\n")

spreadsheet_id = '1mlNDWs__ncSwFBGl6xQkwKUQj9RWSQfsvIvxh_CCh5g'
call_to_action_middle = '<Призыв к действию 1>'
call_to_action_end = '<Призыв к действию 2>'
keywords = "<ключевые слова от пользователя>"
