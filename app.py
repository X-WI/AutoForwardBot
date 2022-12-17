
import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from info import Info
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class LxAutoEdit(Client):
    
    def __init__(self):
        super().__init__(
            name="Auto-edit",
            bot_token = Config.BOT_TOKEN,
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            workers = 20,
            plugins = dict(
                root="LxAutoEdit"
            )
        )

if __name__ == "__main__" :
    LxAutoEdit().run()
