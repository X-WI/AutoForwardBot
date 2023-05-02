import os, asyncio, logging
from pyrogram import filters, enums
import logging
logger = logging.getLogger(__name__)
from main import Bot

media_filter = filters.document | filters.video 

@Bot.on_message(filters.chat(-1001667023505) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001842801591, 
            from_chat_id=-1001667023505, 
            message_id=update.id, 
            caption=f"**{update.caption}**",          
            parse_mode=enums.ParseMode.MARKDOWN                     
        )    
    except Exception as e:
        logger.exception(e)

@Bot.on_message(filters.chat(-1001277498778) & media_filter)
async def forward2(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001842801591, 
            from_chat_id=-1001277498778, 
            message_id=update.id, 
            caption=f"**{update.caption}**",          
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except Exception as e:
        logger.exception(e)
        
      
