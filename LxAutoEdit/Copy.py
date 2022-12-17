import os, time
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums 
from info import Info
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@Client.on_message(filters.media)
async def forward(bot, update):
    try:
        await bot.copy_message(
            chat_id=Info.CHANNEL_ID,
            from_chat_id=update.chat.id,
            message_id=update.id,
            caption=update.caption
        )
    except FloodWait as e:
        time.sleep(e.value)
