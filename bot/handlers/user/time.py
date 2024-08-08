from aiogram.types import Message
from loader import dp
from data.weather import get_weather_hours

@dp.message(lambda message: message.text  == '/time')
async def week_handler(message: Message) -> None:
    try:
        await message.answer(get_weather_hours())
    except TypeError:
        await message.answer("idk")