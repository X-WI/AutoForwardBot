from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('📜 Channel', url='https://t.me/DFF_UPDATES'),
        InlineKeyboardButton('Owner ♻️', url='https://t.me/Lx_0980')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text="Auto forward <b>DFF_UPDATE</b> to <b>WebxZone</b>",              
        parse_mode=enums.ParseMode.HTML)
