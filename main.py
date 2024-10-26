import asyncio
import logging
import sys
from os import getenv
import requests

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


def gamma_auth(username, password):
    url = "https://api.gamma.co.uk/auth/token"
    # url = "https://api-test.gamma.co.uk/auth/token" # test server
    
    data = f"grant_type=password&username={username}&password={password}"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response Text:", response.text)



us = "koket"
password = "koket123Q%"

gamma_auth(us, password)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())