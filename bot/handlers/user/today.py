from aiogram.types import Message
from loader import dp
from data.weather import get_weather_day

@dp.message(lambda message: message.text  == '/today')
async def today_handler(message: Message) -> None:
    try:
        await message.answer(get_weather_day())
    except TypeError:
        await message.answer("idk")