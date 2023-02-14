"""TElegram CHannel parsER app starting point module."""

import asyncio
from pyrogram import Client
from config_reader import load_config


async def startup():
    config = load_config('bot.ini')
    bot = Client('techer', config.api_id, config.api_hash)
    async with bot:
        await bot.send_message('me', 'Greetings!')


if __name__ == '__main__':
    asyncio.run(startup())
