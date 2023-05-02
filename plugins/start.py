from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('📜 Channel', url='https://t.me/Lx0980AI'),
        InlineKeyboardButton('Owner ♻️', url='https://t.me/Lx0980BOT')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text="Hello there, my name is Auto Caption Bot! I can edit Channel media Caption. <b>Developer: @Lx0980AI</b>",              
        parse_mode=enums.ParseMode.HTML)
