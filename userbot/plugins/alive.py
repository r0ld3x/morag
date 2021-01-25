from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ultron"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/2ebd844b4c5ef8c458b8c.jpg"

pm_caption = f"🔅 🔅 🔅HEY I AM [MORAG](https://t.me/MORAGMODS)🔅 🔅 🔅 THE PRIVATE ASSISTANT OF MY MASTER [{DEFAULTUSER}](tg://user?id={kraken}) \n\n"

pm_caption += "MY TELETHON VERSION: 1.15.0 \n"

pm_caption += "MY PYTHON VERSION: 3.7.4 \n"

pm_caption += "[✨REPO✨](https://github.com/r0ld3x/morag) 🔹 [📜License📜](https://github.com/r0ld3x/morag/blob/master/LICENSE)\n\n"

pm_caption += "🔅🔅🔅©MORAG PRIME™🔅🔅🔅"



@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add()
