import asyncio
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from buttons import menu, fanlar, sinflar
from sinf import sinf_soni

# ======================
# ENV YUKLASH
# ======================
load_dotenv()
TOKEN = getenv("BOT_TOKEN")
ADMIN_ID = int(getenv("ADMIN_ID"))  # Telegram ID

dp = Dispatcher()
bot = Bot(token=TOKEN)


# ⭐ /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Assalomu aleykum {message.from_user.full_name}\nMenulardan birini tanlang:",
        reply_markup=menu
    )


# ⭐ Maktab haqida
@dp.message(F.text == "1-maktab haqida🏨")
async def about(msg: Message):
    await msg.answer(
        "🏫 1-sonli maktab — sifatli ta’lim beruvchi zamonaviy ilm maskani."
    )


# ⭐ Fanlar
@dp.message(F.text == "📚Fanlar")
async def courses(msg: Message):
    await msg.answer("Maktab darsliklari📖:", reply_markup=fanlar)


# ⭐ Sinflar
@dp.message(F.text == "Sinflar")
async def classes(msg: Message):
    await msg.answer("Maktabimiz sinflari:", reply_markup=sinflar)


# ⭐ SINFLAR SONI
@dp.message(F.text.in_(sinf_soni.keys()))
async def sinf_soni_chiqar(msg: Message):
    sinf = msg.text
    soni = sinf_soni[sinf]
    await msg.answer(f"📚 {sinf} sinfida {soni} ta o‘quvchi bor")


# ⭐ Orqaga
@dp.message(F.text == "🔙orqaga")
async def back(msg: Message):
    await msg.answer("Asosiy menyu:", reply_markup=menu)


# ⭐ Manzil
@dp.message(F.text == "📍Manzilimiz")
async def location(msg: Message):
    await msg.answer("Bizning manzilimiz:")
    await msg.answer("Sirdaryo viloyati, Mirzaobod tumani, Yangi hayot mahallasi")



# ⭐ TELEFON QABUL QILISH (📞 NOMER QOLDIRISH)
@dp.message(F.contact)
async def send_contact(msg: Message):
    phone = msg.contact.phone_number
    name = msg.contact.full_name
    username = msg.from_user.username

    matn = f"📥 Yangi ariza\n👤 Ismi: {name}\n📱 Nomeri: {phone}\n🔗 Username: @{username}"

    try:
        await bot.send_message(chat_id=ADMIN_ID, text=matn)
    except Exception as e:
        print("Xabar yuborilmadi:", e)

    await msg.answer("Rahmat ❤️ Tez orada siz bilan bog‘lanamiz.")


# ⭐ Botni ishga tushirish
async def main():
    print("Bot ishga tushdi...")
    # ⭐ skip_updates=True bilan polling
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())