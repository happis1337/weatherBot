from aiogram import types
from loader import bot


async def set_default_commands():
    await bot.set_my_commands(
        [
            types.bot_command.BotCommand(command="start", description="bot started"),
            types.bot_command.BotCommand(command="help", description="help"),
            types.bot_command.BotCommand(command="today", description="today weather"),
            types.bot_command.BotCommand(command="tomorrow", description="tomorrow weather"),
            types.bot_command.BotCommand(command="week", description="weather next week")
        ]
    )
