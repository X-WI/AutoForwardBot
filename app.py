import logging
import pyrogram
from pyrogram import Client, filters, enums

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


media_filter = filters.document | filters.video | filters.audio
usercaption_position = "top"
caption_position = usercaption_position.lower()
caption_text = "@HQFilms4U"


class LxAutoEdit(Client):
    
    def __init__(self):
        super().__init__(
            name="Auto-edit",
            bot_token="5300015911:AAE0jwmVovvrv6zH9dC8TfE5-UlFIVOyX78",
            api_id=26686963,
            api_hash="7cce2717e7e89eb534b7da973926f6c4",                        
        )




@Client.on_message(filters.command("start") & filters.incoming)
async def start(bot, message):
        await message.reply("TG Automation Bot")


@Client.on_message(media_filter)
async def editing(bot, message):
      try:
         media = message.document or message.video or message.audio
         caption_text = "@HQFilms4U"
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


if __name__ == "__main__" :
    LxAutoEdit().run()
