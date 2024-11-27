from aiogram import types

from router import router 
from loader import db

@router.callback_query(lambda call: "save" in call.data)
async def start(call: types.CallbackQuery):
    city_name = call.data.split(":")[-1].capitalize()
    
    try:
        db.register_city(telegram_id=call.from_user.id, city_name=city_name)
        await call.message.answer(text="Shahar saqlandi")

    except:
        await call.answer(text="Shahar allaqachon saqlangan", show_alert=True)

