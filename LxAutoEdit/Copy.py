import os, time
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums 
from info import Info

media_filter = filters.document | filters.video | filters.audio

@Client.on_message(media_filter)
async def forward(bot, update):
    try:
        await bot.copy_message(
            chat_id =Info.CHANNEL_ID,
            from_chat_id=update.chat.id,
            message_id=update.id,
            caption=update.caption
        )
    except FloodWait as e:
        time.sleep(e.value)
