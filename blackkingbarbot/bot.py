import asyncio
from aiogram import Bot
from aiogram import Dispatcher
from app.handlers import router


async def main():
    bot = Bot(token='7292385669:AAEORxmkHbDOGv0zdHOAaGvyK90IXrIEL2E')

    await bot.delete_webhook()

    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')