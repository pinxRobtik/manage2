import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Hikari.events import register
from Hikari import telethn as tbot


PHOTO = "https://telegra.ph//file/e6a2b9318171a2743393f.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴀᴋᴜ sᴀᴢᴀ ꭙ ꝛᴏʙᴏᴛ.** \n\n"
  TEXT += "๏ **ᴀᴋᴜ sᴇʟᴀʟᴜ ʜɪᴅᴜᴘ ᴅᴀɴ ʙᴇᴋᴇʀᴊᴀ** \n\n"
  TEXT += f"๏ **ᴍʏ ᴏᴡɴᴇʀ : [ℝ 𝔼 ℤ 𝔸](https://t.me/kenapazaa)** \n\n"
  TEXT += f"๏ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"๏ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"๏ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴋᴜ ᴅɪsɪɴɪ 🔥**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/sazamusicrobot?start=help"), Button.url("ᴅᴏɴᴀsɪ ​", "https://t.me/kenapatagkazu")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
