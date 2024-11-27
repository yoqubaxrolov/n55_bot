from aiogram import types
from requests import get as GET

from config import OPEN_WEATHER_API_TOKEN
from router import router
from keyboards.inline.save_city import generate_save_city_menu


def get_weather_data(city_name):
    PARAMS = {
        "q": city_name,
        "appid": OPEN_WEATHER_API_TOKEN,
        "units": "metric",
    }

    response = GET(url=f"https://api.openweathermap.org/data/2.5/weather", params=PARAMS)

    if not response.ok:
        return None

    data = response.json()
    text = ""

    text += f"Bugun <b>{city_name}</b> da\n\n"
    text += f"Harorat : {data['main']['temp']} C\n"
    text += f"Min. harorat : {data['main']['temp_min']} C\n"
    text += f"Max. harorat : {data['main']['temp_max']} C\n\n"

    text += f"Bosim : {data['main']['pressure']} Pa\n"
    text += f"Namlik : {data['main']['humidity']} %\n\n"

    text += f"Quyosh chiqish vaqti : {data['sys']['sunrise']}\n"
    text += f"Quyosh botish vaqti : {data['sys']['sunset']}\n"

    return text

@router.message()
async def fetch_weather_data(message: types.Message):
    city_name = message.text

    data = get_weather_data(city_name)

    if data:
        await message.reply(text=data, parse_mode="HTML",
                    reply_markup=generate_save_city_menu(city_name=city_name))

    else:
        await message.reply(" Shahar topilmadi ")

