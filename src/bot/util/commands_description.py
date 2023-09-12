from aiogram.types import BotCommand

COMMANDS_DESCRIPTION = (
    ("start", "Перезапустить бота"),
    ("help", "Помощь и справка")
)

async def register_commands_description(bot):
    cmd_description = [
        BotCommand(command=cmd[0], description=cmd[1]) for cmd in COMMANDS_DESCRIPTION
        ]
    await bot.set_my_commands(commands=cmd_description)