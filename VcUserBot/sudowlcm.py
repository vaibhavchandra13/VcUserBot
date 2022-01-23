from pyrogram import Client, emoji, filters
from config import HNDLR, SUDO_USERS
from pyrogram.types import Message

@Client.on_message(filters.new_chat_members & filters.user(SUDO_USERS))
async def sudowlcm(client, m: Message):
    await m.reply_text("**Hey Here Joined My SUDO User**")
