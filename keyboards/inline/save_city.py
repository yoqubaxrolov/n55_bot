from aiogram.utils.keyboard  import InlineKeyboardBuilder


def generate_save_city_menu(city_name):
    builder = InlineKeyboardBuilder()
    
    builder.button(text="Shaharni saqlab qo'yish", callback_data=f"save:{city_name}")
    
    return builder.as_markup()