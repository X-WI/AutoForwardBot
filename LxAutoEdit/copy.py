import os, asyncio,logging
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


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
      try:                       await bot.copy_message(
                 chat_id=CHANNEL_ID, 
                 from_chat_id=update.chat.id,
                 message_id=update.id,
                 caption=update.caption  + "\n" + replace_text,                
                 parse_mode=enums.ParseMode.MARKDOWN,
             )

      except FloodWait as e:
          await asyncio.sleep(e.value)
