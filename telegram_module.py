
import asyncio
from telegram import Bot

class Telegram_Module:
    def __init__(self, api_token, grp_chat_id):
        self.bot_token = api_token
        self.grp_chat_id = grp_chat_id
    async def send_test_message(self, message):

        bot = Bot(token=self.bot_token)
        await bot.send_message(chat_id=self.grp_chat_id,text=message)
