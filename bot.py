import asyncio
from aiogram import Bot, Dispatcher
import questions, different_types
### для лога
from csv_create import creating
from log import writing_scv


# Запуск бота
async def main():
    bot = Bot(token="ВАШ НОМЕР")
    dp = Dispatcher()

    dp.include_router(questions.router)
    dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

#для лога
path = 'Robotmagazine.csv'
valid = exists(path)
if not valid:
   creating()