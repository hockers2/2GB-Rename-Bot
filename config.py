"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hello 👋🏻 {} ❤️,\nI'm An HG Anime Official Rename Bot. This is An Advanced and Yet Powerful Rename Bot.\nFor More Details Check /help\n\n➠ You Can Rename File / Video.\n➠ Change Thumbnail of Your File / Video.\n➠ Convert Video to File & File to Video.\nOur Bot Fully customisable\n➠ Permanent Thumbnail 🖼️ and Custom Caption ✍🏻.\n\nMaintenance By :- [HG_Movies](https://t.me/HG_Movies)</b>"""

    ABOUT_TXT = """<b>🤖 My Name :- {}\n
🧑🏻‍💻 Developer :- <a href=https://t.me/TG_Karthik><b>Karthik</b></a>\n
📝 Language :- Python3\n
📚 Framework :- Pyrogram\n
📡 Hosted on :- VPS\n
💾 Database :- <a href=https://cloud.mongodb.com/>Mongo DB</a>\n
🎥 Movie Updates :- <a href=https://t.me/HG_Movies><b></b>Star Movies Tamil</a>\n
🤖 Bot Channel :- <a href=https://t.me/HG_Movies><b></b>Star Bots Tamil</a></b>"""

    HELP_TXT = """
<b><u>Available Commands</u>

➠ /start :- Check if 😊 I'm Alive
➠ /help :- How to Use❓
➠ /about :- to Know About Me 😌
    
🖼️ <u>How to Set Thumbnail</u>
 
➠ /start The Our Bot And Send Any Photo to Automatically Set Thumbnail 🖼️
➠ /showthumbnail :- View Current Thumbnail 🖼️
➠ /deletethumbnail :- Delete 🗑️ Your Thumbnail 🖼️

✍🏻 <u>How to Set Custom Caption</u>

➠ /set_caption :- Set Custom Caption ✍🏻
➠ /see_caption :- View Current Caption ✍🏻
➠ /del_caption :- Delete 🗑️ Your Caption
Example :- `/set_caption 📁 File Name :- {filename}

💾 File Size :- {filesize}

⏰ Duration :- {duration}`

✏️ <u>How to Rename File</u>

➠ Send me Any File And Type New File Name

<u>📂 Supported File Formats</u>

➠ 📁 Document
➠ 🎥 Video
➠ 🎵 Audio

⚠️ Contact For Any Problem :- [👥 Support Group](https://t.me/+eSMjCIJITH5lMTRl)</b>"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    DEV_TXT = """<b><u>Special Thanks & Developer</b></u>
<b>🧑🏻‍💻 Developer :- </b><a href=https://t.me/HG_ASSISTANT><b>Owner</b></a>"""

    PROGRESS_BAR = """<b>\n
🚀 Speed :- {3}/sec\n
💯 Percentage :- {0}%\n
✅ Done :- {1}\n
💾 Size :- {2}\n
⏰ Time Left :- {4}\n\n©️ [HG Anime](https://t.me/HG_Movies)</b>"""


