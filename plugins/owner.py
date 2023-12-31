from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid, UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty

from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, WELCOM_PIC, WELCOM_TEXT, IMDB_TEMPLATE
from utils import get_size, temp, extract_user, get_file_id, get_poster, humanbytes
from database.users_chats_db import db
from database.ia_filterdb import Media
from datetime import datetime
from Script import script
import logging, re, asyncio, time, shutil, psutil, os, sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command('owner') & filters.incoming)
async def get_ownr(bot, message):
    own = await message.reply(script.PROGRAMMER_TXT)
    await rju.edit(InputMediaPhoto(random.choice(PICS2),script.PROGRAMMER_TXT))