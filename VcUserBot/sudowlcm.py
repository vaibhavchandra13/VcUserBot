from pyrogram import Client, emoji, filters
from config import HNDLR, SUDO_USERS


@Client.on_message(filters.new_chat_members & filters.user(SUDO_USERS))
async def sudowlcm(client, message: Message):
    m.reply_text("**Hey Here Joined My SUDO User**")
