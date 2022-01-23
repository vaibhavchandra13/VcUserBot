from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS
from VcUserBot.helpers.get_file_id import get_file_id


@Client.on_message(filters.command(["id"], prefixes=f"{HNDLR}"))
async def showid(_, message: Message):
    chat_type = message.chat.type
    chat_id = m.chat.id
    if not await CHATS:
        await message.reply_text(f"**This is A Music Bot Made Only for Private Use in Some Specific Chats**")
        return await Client.leave_chat(chat_id) 
    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>ID group</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>ID Replied user</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>ID User</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
