import logging
import pyrogram
from pyrogram import Client, filters, enums
from info import Info

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class lxautoedit(Client):
    
    def __init__(self):
        super().__init__(
            name = "Auto-edit",
            bot_token = Info.BOT_TOKEN,
            api_id = Info.API_ID,
            api_hash = Info.API_HASH,           
            workers = 20,
            plugins = dict(
                root="LxAutoEdit"
            )
        )


