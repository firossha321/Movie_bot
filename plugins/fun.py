import os, re, json, base64, logging, random, asyncio

from Script import script
import time
from info import COMMAND_HAND_LER
from database.users_chats_db import db
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from info import CHANNELS, ADMINS, AUTH_CHANNEL, TOSS, LOG_CHANNEL, DISE, PICS, PICS2, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT, START_MESSAGE, FORCE_SUB_TEXT, SUPPORT_CHAT
from utils import get_settings, get_size, is_subscribed, save_group_settings, temp
from database.connections_mdb import active_connection

logger = logging.getLogger(__name__)
BATCH_FILES = {}

@Client.on_message(filters.command("toss")) 
async def toss(client, message):
    cap1="ᴛʜɪꜱ ɪꜱ ʏᴏᴜʀ ʀᴇꜱᴜʟᴛ"
    firos = await message.reply_sticker("CAACAgIAAxkBAAIVrmW44AABninrQsje8r0Nvl-EoJPn0AACvgkAAoSumEoSQwToTbAzsh4E") 
    time.sleep(3)
    await message.reply_photo(photo=random.choice(TOSS),caption=cap1)
    await firos.delete()


DICE_E_MOJI = "🎲"
cap2="ᴛʜɪꜱ ɪꜱ ʏᴏᴜʀ ꜱᴄᴏʀᴇ"
@Client.on_message(filters.command(["dise", "dice"], COMMAND_HAND_LER))
async def roll_dice(client, message):
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id
    kel = await client.send_dice(chat_id=message.chat.id,emoji=DICE_E_MOJI,disable_notification=True,reply_to_message_id=rep_mesg_id)
    time.sleep(4)
    await message.reply_photo(photo=random.choice(DISE),caption=cap2)
    await kel.delete()
