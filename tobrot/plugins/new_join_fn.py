#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    #channel_id = str(AUTH_CHANNEL)[4:]
    #message_id = 99
    # display the /help
    
    await message.reply_text("""join this group forr help-- @requestinggroup\n\n ytdl - This command should be used as reply to a supported link
pytdl - This command will download videos from youtube playlist link and will upload to telegram.
ytdl gdrive - This will download and upload to google drive
pytdl gdrive - This download youtube playlist and upload to google drive
leech - to leech to telegram
leech archive - to leech and archive
gleech - download and upload to gdrive
gleech archive - This command will compress the folder/file and will upload to gdrive
leech unzip - This will unzip the .zip file and dupload to telegram
gleech unzip - This will unzip the .zip file and upload to gdrive
leech unrar - This will unrar the .rar file and dupload to telegram
gleech unrar - This will unrar the .rar file and upload to gdrive
leech untar - This will untar the .tar file and upload to telegram
gleech untar - This will untar the .tar file and upload to gdrive
tleech - This will mirror the telegram files to ur respective cloud cloud
tleech unzip - This will unzip the .zip telegram file and upload to gdrive
tleech unrar - This will unrar the .rar telegram file and upload to gdrive
tleech untar - This will untar the .tar telegram file and upload to gdrive
getsize - This will give you total size of your destination folder in gdrive
renewme -  This will clear the remains of downloads which are not getting deleted after upload of the file or after /cancel command.""", disable_web_page_preview=True)


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/keralagram/698909"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
