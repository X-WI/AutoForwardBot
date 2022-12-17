import logging
import pyrogram
from pyrogram import Client, filters, enums

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class lxautoedit(Client):
    
    def __init__(self):
        super().__init__(
            name="Auto-edit",
            bot_token="5300015911:AAE0jwmVovvrv6zH9dC8TfE5-UlFIVOyX78",
            api_id=26686963,
            api_hash="7cce2717e7e89eb534b7da973926f6c4",                        
            workers = 20,
            plugins = dict(
                root="Plugins"
            )
        )

if __name__ == "__main__" :
    lxautoedit().run()
        
