import asyncio
import os
from pytgcalls import idle

from config import call_py





async def main():
    os.system('apt update && apt upgrade -y && apt install ffmpeg -y && curl -sL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs && npm i -g npm && pip3 install -U -r requirements.txt')
    await call_py.start()
    print(
        """
    ------------------
   | VcUserBot Started! |
    ------------------
"""
    )
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
