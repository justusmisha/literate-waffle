from aiogram.utils import executor


async def on_startup(dp):
    from utils.set_botcommands import set_default_commands
    await set_default_commands(dp)


if __name__ == "__main__":
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
