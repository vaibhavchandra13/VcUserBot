import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, bot


@Client.on_message(filters.command(["join"], prefixes=f"{HNDLR}"))
async def join(client: Client, m: Message):
  msg = await m.reply_text("Join Chat...")
  chaturl = m.text.split(None, 1)[1]
  client.join_chat(chaturl)
  await msg.edit("Joined...")
