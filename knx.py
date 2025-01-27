import asyncio
from xknx import XKNX
from xknx.tools import group_value_write

async def main():
    async with XKNX() as xknx:
        # send a binary Telegram
        group_value_write(xknx, "1/2/3", True)
        # send a generic 1-byte Telegram
        group_value_write(xknx, "1/2/4", [0x80])
        # send a Telegram with an encoded value
        group_value_write(xknx, "1/2/4", 50, value_type="percent")

asyncio.run(main())
