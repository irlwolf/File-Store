#(©)t.me/Outlawbots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8139084920:AAH-2pX1yZLEw6UeqbhJtshQ95esk-zP_s0")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23580732"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "81ca3df48f25d954b2ebef5aec715a73")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002409821863"))
#OWNER USERNAMA OWNER
OWNER = os.environ.get("OWNER", "irlwolf")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1302460619"))
# OWNER USERNAME WITHOUT @ REQUIRED 
OWNER_USER = os.environ.get("OWNER_USER", "irlwolf")
#Port
PORT = os.environ.get("PORT", "8080")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://irlwolf:9aEpUre0fkmBjHVz@cluster0.jkd3o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "irlwolf")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002470891127"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001524582676"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://ibb.co/wZmCvV5M")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://ibb.co/wZmCvV5M")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @serieswolftamil\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/HateXfree>ᯓ ʜᴀᴛᴇ ғʀᴇᴇ ᡣ𐭩</a></b>"
#Change This Person link 😂 important!!
ABOUT_TXT = f"""<b><blockquote>╭───────────⍟
├➤ ᴄʀᴇᴀᴛᴏʀ  : <a href='t.me/InkaLinks'>ᴛʜɪs ᴘᴇʀsᴏɴ</a>
├➤ ʟɪʙʀᴀʀy : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a>
├➤ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 3</a>
├➤ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/outlawbots>ᴏᴜᴛʟᴀᴡ ʙᴏᴛs</a>
├➤ ᴘᴀɪᴅ ʙᴏᴛ : <a href=https://t.me/ifeelscam>ᯓ ɪɴᴠᴀʟɪᴅ ᡣ𐭩</a>
├➤ ᴅᴇᴠʟᴏᴘᴇʀ : <a href=https://t.me/HateXfree>ᯓ ʜᴀᴛᴇ ғʀᴇᴇ ᡣ𐭩</a>
╰───────────────⍟</blockquote></b>"""
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʏ !! {first}\n\n <blockquote>ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "1302460619").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message ,for mention {mention} , for first name {first} , for username {username}
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b><blockquote>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʀʏ ᴀɢᴀɪɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</blockquote></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @OutlawBots</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Dᴏɴ'ᴛ sᴇɴᴅ ᴍᴇ ᴍᴇssᴀɢᴇs ᴅɪʀᴇᴄᴛʟʏ ɪ'ᴍ ᴏɴʟʏ ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ!"

ADMINS.append(OWNER_ID)
ADMINS.append(1302460619)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
