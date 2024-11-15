import os
from dotenv import load_dotenv

load_dotenv()

BASE_URLS = os.getenv('BASE_URLS')

BOT_TOKEN = list(os.getenv('BOT_TOKEN'))

# categories = ["Личные вещи", "Транспорт", "Недвижимость", "Работа", "Услуги", "Для дома и дачи", "Бытовая электроника",
#               "Хобби и отдых", "Животные", "Для бизнеса"]

PARSING_MESSAGE = 'Парсим 👨‍💻'

categories = ["👕 Личные вещи", "🗣 Услуги",
              "🏡 Для дома и дачи", "🛠 Бытовая электроника",
              "🔑 Генератор ключевых слов", "◀️ Назад"]

start_buttons_list = ["📊 Анализ рыночной ситуации", "🤖 Генерация"]

prompt_common_en_1 = "###Instructions:\nYou are a copywriter and write selling ads for avito about "

prompt_common_en_2 = " now you need to write a text for a locational ad for category "

prompt_common_en_3 = ", keep in mind that the ad should have such a structure: a short title, tell about the "

prompt_common_en_4 = (". Then make call to  write to avito or make phone call, then the benefits and completion too "
                      "with a "
                      "request to save the ad to favorites. Use emojis to increase the readability of "
                      "the text. Don't use such symbols as * and \". Be sure that all your suggestions and thoughts "
                      "come to a logical end.\n")

spreadsheet_id = os.getenv('SPREADSHEET_ID')
call_to_action_middle = '<Призыв к действию 1>'
call_to_action_end = '<Призыв к действию 2>'
keywords = "<ключевые слова от пользователя>"
