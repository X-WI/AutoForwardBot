import logging
import pyrogram
from pyrogram import Client, filters, enums
from info import Info

"""
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


if __name__ == "__main__" :
    lxautoedit().run()
"""


class Bot(Client):

    def __init__(self):
        super().__init__(
            "bot",
            api_hash=Info.API_HASH,
            api_id=Info.API_ID,
            plugins={
                "root": "LxAutoEdit"
            },
            workers=200,
            bot_token=Info.BOT_TOKEN,
            sleep_threshold=10
        )


app = Bot()
app.run()
