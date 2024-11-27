from aiogram import types
from aiogram.filters.command import CommandStart

from router import router
from loader import db


@router.message(CommandStart())
async def start(message: types.Message):
    telegram_id = message.from_user.id
    fullname = message.from_user.full_name
    username = message.from_user.username

    try:
        db.register_user(telegram_id, fullname, username)
        await message.reply(text=f"Assalomu alaykum, {fullname}\n\nSiz muvaffaqiyatli ro'yxatga olindingiz !")
    except:
        await message.answer(text=f"Qaytganingiz bilan {fullname}")

