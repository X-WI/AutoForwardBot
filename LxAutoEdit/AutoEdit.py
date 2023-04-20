# @Lx_0988
import logging
from info import Info
from pyrogram import Client, filters, enums
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


media_filter = filters.document | filters.video | filters.audio
usercaption_position = "top"
caption_position = usercaption_position.lower()
caption_text = "@TheDXClassic"

@Client.on_message(filters.channel & (media_filter))
async def editing(bot, message):
      try:
         media = message.document or message.video or message.audio
         caption_text = "@TheDXClassic"
      except:
         caption_text = ""
         pass 
      if (message.document or message.video or message.audio): 
          if message.caption:                        
             file_caption = f"**{message.caption}**"                
          else:
             fname = media.file_name
             filename = fname.replace("_", ".")
             file_caption = f"`{filename}`"  
              
      try:
          if caption_position == "top":
             await bot.edit_message_caption(
                 chat_id=message.chat.id, 
                 message_id=message.id,
                 caption=file_caption + "\n\n" + f"**{caption_text}**", 
                 parse_mode=enums.ParseMode.MARKDOWN
             )

      except:
          pass
