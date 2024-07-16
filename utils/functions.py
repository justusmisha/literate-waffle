import random
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from data.config import call_to_action_middle, call_to_action_end


def text_formating(text):
    text = text.replace('**', '')
    text = text.replace('*', '')
    return text


def google_prompts(category):
    try:
        spreadsheet_id = '1mlNDWs__ncSwFBGl6xQkwKUQj9RWSQfsvIvxh_CCh5g'
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


def get_call_to_action():
    try:
        spreadsheet_id = '1X1q8qIhii0_mtUzPDN5vb0vYZdiiHgb1735f2Vloh1A'
        range_name = f'Призывы Услуги!A1:A27'

        creds = Credentials.from_authorized_user_file(
            'token.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )

        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])
        list_values = []
        for row in values:
            list_values.append(''.join(row))
        if len(list_values) >= 2:
            return random.sample(list_values, 2)
        else:
            return list_values[0]
    except Exception as e:
        print(e)


def text_checker(text):
    try:
        calls_to_action = get_call_to_action()

        if not isinstance(calls_to_action, list):
            calls_to_action = [calls_to_action]

        if call_to_action_middle in text:
            replacement = calls_to_action[0] if len(calls_to_action) >= 1 else ''
            text = text.replace(call_to_action_middle, replacement)

        if call_to_action_end in text:
            replacement = calls_to_action[1] if len(calls_to_action) >= 2 else calls_to_action[0] if len(calls_to_action) >= 1 else ''
            text = text.replace(call_to_action_end, replacement)

        return text
    except Exception as e:
        print(e)
        return text

