import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
HNDLR = list(os.getenv("HNDLR").split())
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", None)
OFFICIAL_UPSTREAM_REPO = os.getenv("OFFICIAL_UPSTREAM_REPO", "https://github.com/vaibhavchandra13/VcUserBot")

contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VcUserBot"))
call_py = PyTgCalls(bot)

