import asyncio
import os
from pytgcalls import idle

from config import call_py, bot





async def main():
    await bot.run()
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
