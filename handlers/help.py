from aiogram import types
from aiogram.filters.command import Command

from router import router


@router.message(Command("help"))
async def help(message: types.Message):
    await message.reply("Sizga qanday yordam bera olaman ?")