from aiogram import Bot, Dispatcher

from handlers.handler import router_calendar

TOKEN = ""

bot: Bot = Bot(TOKEN)
dp: Dispatcher = Dispatcher()


dp.include_router(router_calendar)


if __name__ == "__main__":
    dp.run_polling(bot)

