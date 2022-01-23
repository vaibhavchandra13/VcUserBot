import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, bot, SUDO_USERS, CHATS


@Client.on_message(filters.command(["join"], prefixes=f"{HNDLR}") & filters.user(SUDO_USERS))
async def join(client: Client, m: Message):
  chat_id = m.chat.id
  if not await CHATS:
        await message.reply_text(f"**This is A Music Bot Made Only for Private Use in Some Specific Chats**")
  replied = m.reply_to_message
  if replied:
        msg = await m.reply_text("Joining Chat...")
        chaturl = m.reply_to_message.text.split()
        await client.join_chat(chaturl)
        await msg.edit("Joined...")
  else
        msg = await m.reply_text("Joining Chat...")
        chaturl = m.text.split(None, 1)[1]
        await client.join_chat(chaturl)
        await msg.edit("Joined...")
