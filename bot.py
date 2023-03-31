from aiogram import Bot, Dispetcher, types, executor
import logging
TOKEN='6128486884:AAGKf6FegfLCUMAfQBt92q51Lwog0UeJYek'
logging.basicConfig(level=logging.INFO)
bot=Bot(token=TOKEN)
dp=Dispetcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__=='__main__':
    executor.start_polling(dp)
