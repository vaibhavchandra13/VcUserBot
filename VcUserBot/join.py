import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, bot, SUDO_USERS


@Client.on_message(filters.command(["join"], prefixes=f"{HNDLR}") & filters.user(SUDO_USERS))
async def join(client: Client, m: Message):
  msg = await m.reply_text("Joining Chat...")
  chaturl = m.text.split(None, 1)[1]
  await client.join_chat(chaturl)
  await msg.edit("Joined...")
