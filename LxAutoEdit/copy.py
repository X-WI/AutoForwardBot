import os, asyncio

from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums

CHANNEL_ID = 1001743048821
replace_text = "@Lx0980"
"""
@Client.on_message(filters.media)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001743048821,
            from_chat_id=update.chat.id,
            message_id=update.id,
            caption=update.caption,
            parse_mode=enums.ParseMode.MARKDOWN
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
"""

@Client.on_message(filters.media)
async def forward(bot, update):
      try:
         media = message.document or message.video or message.audio
         replace_text = "@Lx0980"
      except:
         replace_text = ""
         pass 
      if (message.document or message.video or message.audio): 
          if message.caption:                        
             file_caption = f"**{message.caption}**"                

      try:
          if caption_position == "hello":
             await bot.copy_message(
                 chat_id=CHANNEL_ID, 
                 from_chat_id=update.chat.id,
                 message_id=update.id,
                 caption=file_caption + "\n" + replace_text,
                 parse_mode=enums.ParseMode.MARKDOWN
             )
         except FloodWait as e:
             await asyncio.sleep(e.value)
