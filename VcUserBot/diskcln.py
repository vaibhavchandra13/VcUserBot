from pyrogram import Client, emoji, filters
from config import HNDLR, SUDO_USERS
from pyrogram.types import Message
import os, glob


downloads = "./Downloads"
raw = os.path.realpath("raw_files")

@Client.on_message(filters.command(["cleardl"], prefixes=f"{HNDLR}") & filters.user(SUDO_USERS))
async def cleardisk(client, m: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.mp3")
            os.system("rm -rf *.mp4")
            os.system("rm -rf *.m4a")
            os.system("rm -rf *.webm")
        await m.reply_text("**Removed All Downloaded Files**")
    else:
        await m.reply_text("**NO FILES FOUND**")

        
        
@Client.on_message(filters.command(["clearjpg"], prefixes=f"{HNDLR}") & filters.user(SUDO_USERS))
async def clearjpg(client, m: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.jpg")
        await m.reply_text("**Removed All JPG Files**")
    else:
        await m.reply_text("**NO FILES FOUND**")
