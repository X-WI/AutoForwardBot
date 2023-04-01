from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('📜 Channel', url='https://t.me/Lx0980_Official'),
        InlineKeyboardButton('Owner ♻️', url='https://t.me/Lx_0980')
    ],[
        InlineKeyboardButton('SouceCode 💡', url='https://github.com/Lx0988')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.START_TXT.format(
                message.from_user.first_name),
        parse_mode=enums.ParseMode.HTML)
