import asyncio
import re
from datetime import timedelta
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ChatPermissions
from aiogram.filters import Command

# 1. BOT_TOKEN ni shu yerga yozing
TOKEN = "SIZNING_BOT_TOKENINGIZNI_SHU_YERGA_YOZING"

BAD_WORDS = ["yomonsoz", "axmoq", "jinni"]  # O'zgartirib olasiz


def clean_text(text: str) -> str:
    text = text.lower()
    replacements = {'@': 'a', '0': 'o', '1': 'i', '$': 's', '3': 'e'}
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r'[^a-z\'\`ўқғҳ]', '', text)
    return text


def is_bad_message(text: str) -> bool:
    words = text.lower().split()
    for word in words:
        cleaned_word = clean_text(word)
        for bad_word in BAD_WORDS:
            if bad_word in cleaned_word:
                return True
    return False


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Salom! Men guruhni toza saqlovchi va tartib o'rnatuvchi admin botman. \n"
        "Guruhga qo'shing va menga to'liq admin huquqlarini bering!"
    )


@dp.message(F.chat.type.in_({"group", "supergroup"}))
async def group_message_handler(message: Message):
    # 1. Admin tekshiruvi: Xabarni kim yozganini tekshiramiz
    try:
        admins = await bot.get_chat_administrators(message.chat.id)
        admin_ids = [admin.user.id for admin in admins]

        # Agar xabar egasi admin yoki guruh yaratuvchisi bo'lsa, tekshirishni to'xtatamiz
        if message.from_user.id in admin_ids:
            return
    except Exception as e:
        print(f"Adminlarni olishda xatolik: {e}")
        return

    # 2. Havola (Link) borligini aniqlash mantig'i
    has_link = False
    entities = message.entities or message.caption_entities
    if entities:
        for entity in entities:
            # "url" - ochiq havolalar (http...), "text_link" - so'zga yashiringan havolalar
            if entity.type in ("url", "text_link"):
                has_link = True
                break

    # 3. Agar oddiy a'zo havola (link) yoki video tashlasa
    if has_link or message.video or message.video_note:
        try:
            # Xabarni o'chiramiz
            await message.delete()

            # Foydalanuvchini 1 soatga (faqatgina yozish huquqini olib qo'yib) bloklaymiz
            mute_time = timedelta(hours=1)
            await bot.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id,
                permissions=ChatPermissions(can_send_messages=False),
                until_date=mute_time
            )

            warning = await message.answer(
                f"🚫 {message.from_user.full_name}, guruhga video yoki havola tashlash mumkin emas!\n"
                f"Siz 1 soatga 'Mute' (jimlik) rejimiga tushirildingiz."
            )
            # 5 soniyadan keyin ogohlantirishni o'chirish
            await asyncio.sleep(5)
            await bot.delete_message(chat_id=message.chat.id, message_id=warning.message_id)

            return  # Shu yerda kodni to'xtatamiz, so'kinishga tekshirish shart emas

        except Exception as e:
            print(f"Bloklashda xatolik: Botda yetarli huquq yo'q bo'lishi mumkin. Xato: {e}")
            return

    # 4. So'kinishlarni tekshirish (oldingi mantiq)
    if message.text and is_bad_message(message.text):
        try:
            await message.delete()
            warning = await message.answer(
                f"⚠️ {message.from_user.full_name}, guruhda haqoratli so'zlar ishlatish taqiqlangan!")
            await asyncio.sleep(5)
            await bot.delete_message(chat_id=message.chat.id, message_id=warning.message_id)
        except Exception as e:
            print(f"Xatolik: {e}")


async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())