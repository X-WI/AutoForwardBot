import os, asyncio, logging
from pyrogram import filters, enums
import logging
logger = logging.getLogger(__name__)
from main import Bot


dff_caption = "➠ @Hollywood_0980\n➠ @DFF_UPDATES"
media_filter = filters.document | filters.video 

@Bot.on_message(filters.chat(-1001667023505) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001956270124, 
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
            chat_id=-1001956270124, 
            from_chat_id=-1001277498778, 
            message_id=update.id, 
            caption=f"**{update.caption}**",          
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except Exception as e:
        logger.exception(e)
        
        
       
@Bot.on_message(filters.chat(-1001976541395) & media_filter)
async def forward2(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001937462586, 
            from_chat_id=-1001976541395, 
            message_id=update.id, 
            caption=f"**{update.caption}**" + "\n\n" + f"**{dff_caption}**",       
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except Exception as e:
        logger.exception(e)
        
      
