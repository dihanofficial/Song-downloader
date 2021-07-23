#Dihanofficial <https://t.me/dihanofficial>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from DihanOfficialSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DihanOfficialSongBot import DihanOfficialSongBot as app
from DihanOfficialSongBot import LOGGER

pm_start_text = """
Hello there, I'm [Song Downloader Bot 🎵](https://telegra.ph/file/36bae3576c4b9418f4618.jpg)
I'm a Powerful Songs Downloader bot Made by [𝘿𝙞𝙝𝙖𝙣 𝙍𝙖𝙣𝙙𝙞𝙡𝙖 🇱🇰](t.me/dihanrandila)
😉 Just send me the song name you want to download.😋
    
Eg: " /song Despacito "
      
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥰𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 🙋‍♀️", url=f"https://t.me/dihanofficialsongsbot?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 🇱🇰 🛠", url=f"https://t.me/dihanrandila"), 
                    InlineKeyboardButton(
                        "💬 Support", url=f"https://t.me/dihan_official")
                ],[
                    InlineKeyboardButton(
                        "💬 Bots Updates", url=f"https://t.me/dihanofficial")
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info(" DihanOfficialSongBot is online ✅.")
idle()
