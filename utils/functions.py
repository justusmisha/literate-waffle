from data.config import *
import os.path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


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


def text_formating(text):
    text = text.replace('**', '')
    text = text.replace('*', '')
    return text


def google_prompts(category):
    try:
        range_name = f'Промпты!A1:B4'

        creds = Credentials.from_authorized_user_file(
            'token.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )

        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])

        if not values:
            raise ValueError(f'Category "{category}" not found.')
        else:
            for row in values:
                if row[0] == category:
                    return row[1]
            raise ValueError(f'Category "{category}" not found.')
    except Exception as e:
        print(e)
