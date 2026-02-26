from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ASOSIY MENU
menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="1-maktab haqida🏨")],
    [KeyboardButton(text="📚Fanlar"), KeyboardButton(text="Sinflar")],
    [KeyboardButton(text="📞Nomer qoldirish", request_contact=True),
     KeyboardButton(text="📍Manzilimiz")]
], resize_keyboard=True)

# FANLAR
fanlar = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Ona-tili"), KeyboardButton(text="Matematika")],
    [KeyboardButton(text="Adabiyot"), KeyboardButton(text="Tarix")],
    [KeyboardButton(text="Ingliz-tili"), KeyboardButton(text="Rus-tili")],
    [KeyboardButton(text="Geografiya"), KeyboardButton(text="Texnologiya")],
    [KeyboardButton(text="Fizika"), KeyboardButton(text="Geometriya")],
    [KeyboardButton(text="Chizmachilik"), KeyboardButton(text="Informatika")],
    [KeyboardButton(text="Tarbiya")],
    [KeyboardButton(text="🔙orqaga")],
], resize_keyboard=True)

# SINFLAR
sinflar = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="1-'a'"), KeyboardButton(text="1-'b'"), KeyboardButton(text="1-'d'")],
    [KeyboardButton(text="2-'a'"), KeyboardButton(text="2-'b'"), KeyboardButton(text="2-'d'")],
    [KeyboardButton(text="3-'a'"), KeyboardButton(text="3-'b'"), KeyboardButton(text="3-'d'")],
    [KeyboardButton(text="4-'a'"), KeyboardButton(text="4-'b'"), KeyboardButton(text="4-'d'")],
    [KeyboardButton(text="5-'a'"), KeyboardButton(text="5-'b'"), KeyboardButton(text="5-'d'")],
    [KeyboardButton(text="6-'a'"), KeyboardButton(text="6-'b'"), KeyboardButton(text="6-'d'")],
    [KeyboardButton(text="7-'a'"), KeyboardButton(text="7-'b'"), KeyboardButton(text="7-'d'")],
    [KeyboardButton(text="8-'a'"), KeyboardButton(text="8-'b'"), KeyboardButton(text="8-'d'")],
    [KeyboardButton(text="9-'a'"), KeyboardButton(text="9-'b'"), KeyboardButton(text="9-'d'")],
    [KeyboardButton(text="10-'a'"), KeyboardButton(text="10-'b'")],
    [KeyboardButton(text="11-'a'"), KeyboardButton(text="11-'b'")],
    [KeyboardButton(text="🔙orqaga")],
], resize_keyboard=True)