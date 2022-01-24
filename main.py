import asyncio
import os
from pytgcalls import idle

async def main():
    print(
        """
    ------------------
   | VcUserBot Started! |
    ------------------
"""
    )


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
