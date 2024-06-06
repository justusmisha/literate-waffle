import re

from loader import dp



# async def validate_subscription(user_id: int):
#     try:
#         member = await dp.bot.get_chat_member(CHANNEL_ID, user_id)
#         return member.is_chat_member() or member.status in ["creator", "administrator"]
#     except Exception as e:
#         print(f"Error checking subscription: {e}")
#         return False


def validate_name_surname(name_surname):
    return re.match("^[A-Za-zА-Яа-я]{2,15}\s[A-Za-zА-Яа-я]{2,15}$", name_surname)


def validate_phone(phone):
    return re.match("^[0-9]{10,15}$", phone)


def validate_instagram(link):
    if "instagram" not in link and "@" not in link:
        return False
    return True


def validator_for_text(text):
    return not text.isdigit()
