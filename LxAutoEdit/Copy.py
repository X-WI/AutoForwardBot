import os, time
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums 
from info import Info
from typing import Union, Optional, AsyncGenerator
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@Client.on_message(filters.media)
async def forward(bot, update):
    try:
        await bot.copy_message(
            chat_id = Union[Info.CHANNEL_ID],
            from_chat_id = Union[update.chat.id],
            message_id = update.message.id,
            caption = update.caption
        )
    except FloodWait as e:
        time.sleep(e.value)
