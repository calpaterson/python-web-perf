import json
from aiohttp import web
import aiopg
import random

from async_db import get_row

async def handle(request):
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            index = random.randint(1, max_n)
            await cursor.execute("select a, b from test where a = %s", (index,))
            ((a, b),) = await cursor.fetchall()

    return web.Response(text=json.dumps({"a": str(a).zfill(10), "b": b}))


app = web.Application()
app.add_routes([web.get('/test', handle)])
