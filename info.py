import re, time
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default


# PyroClient Setup 
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
TOSS=(environ.get('PICS','https://graph.org/file/93fd874d803bc33cfb625.jpg https://graph.org/file/50c74a43b806c2d1bb649.jpg')).split()
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
SPELL='https://graph.org/file/67b71d8a5e5de086fbed8.jpg'
DISE = (environ.get('DISE','https://graph.org/file/d7cd3555848c13b2ff1fe.jpg https://graph.org/file/93a37346e33c834b6f072.jpg https://graph.org/file/164bc7dbb38e8fbbd78db.jpg https://graph.org/file/8af0bb777756c113086bf.jpg https://graph.org/file/a01669dd9aad20ec3e8d1.jpg https://graph.org/file/8075b4ad6419edf5ea550.jpg')).split()
PICS2 = (environ.get('PICS2' ,'https://graph.org/file/fc82a4680369db51a2564.jpg')).split()
PICS = (environ.get('PICS' ,'https://graph.org/file/9bc905986578fe468ced6.jpg https://graph.org/file/7230540148a6f704552de.jpg https://graph.org/file/1ef334e3cdfa368fae986.jpg https://graph.org/file/b9ffdf56741dcc5c508a7.jpg https://graph.org/file/a4bef533b0ee8815fc2cb.jpg https://graph.org/file/f11a9552706c0b490682f.jpg https://graph.org/file/2df3277be246d91205b4b.jpg https://graph.org/file/c5cbda8edb3f87c3c2639.jpg https://graph.org/file/a4ac39bb700ad227b090f.jpg https://graph.org/file/1aadf3219407df6a5aa4d.jpg https://graph.org/file/375fe73f23f6c6c099e80.jpg https://graph.org/file/10b80b514219cbded6e9e.jpg https://graph.org/file/a291f637768262bd52f5e.jpg')).split()
UPTIME = time.time()

COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# Admins, Channels & Users
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
PREMIUM = int(environ.get('PREMIUM', ""))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1002093025125')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
FILE_DB_URL = environ.get("FILE_DB_URL", DATABASE_URL)
FILE_DB_NAME = environ.get("FILE_DB_NAME", DATABASE_NAME)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Filters Configuration 
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', script.START_TXT)
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)

WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", script.WELCOM_TEXT)
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)
RemoveBG_API = environ.get("RemoveBG_API", "")

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MKN_BOTZ_DISCUSSION_GROUP')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
