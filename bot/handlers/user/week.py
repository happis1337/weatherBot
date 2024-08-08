from aiogram.types import Message
from loader import dp
from data.weather import get_weather_week

@dp.message(lambda message: message.text  == '/week')
async def week_handler(message: Message) -> None:
    try:
        await message.answer(get_weather_week())
    except TypeError:
        await message.answer("idk")