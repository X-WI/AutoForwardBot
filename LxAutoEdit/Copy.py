import os, time
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from info import Info

@Client.on_message(filters.media)
async def forward(bot, update):
    try:
        await bot.copy_message(
            chat_id=Info.CHANNEL_ID,
            from_chat_id=update.chat.id,
            message_id=update.message.id,
            caption=update.caption
        )
    except FloodWait as e:
        time.sleep(e.value)
