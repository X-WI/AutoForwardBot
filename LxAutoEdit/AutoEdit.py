# @Lx_0988
import logging
from info import Info
from pyrogram import Client, filters, enums
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


usercaption_position = "top"
caption_position = usercaption_position.lower()
caption_text = Info.CAPTION_TXT

@Client.on_message(filters.command("start") & filters.incoming)
async def start(bot, message):
        await message.reply("Hello there, I'm Auto Caption Bot! Join @Lx_0980")


@Client.on_message(filters.channel)
async def editing(bot, message):
      try:
         media = message.document or message.video or message.audio
         caption_text = Info.CAPTION_TXT
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
                 caption=file_caption + "\n" + caption_text,
                 parse_mode=enums.ParseMode.MARKDOWN
             )

      except:
          pass
