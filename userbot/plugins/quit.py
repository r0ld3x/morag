"""
.kickme
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from userbot.utils import admin_cmd


@borg.on(admin_cmd("kickme", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**HEY MY MASTER IS LEAVING THIS GROUP** 🤧🤧🤧🖕🏼")
        time.sleep(1)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("**Sir Please Join A group ?😑**")
