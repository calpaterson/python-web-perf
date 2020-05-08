import aiosqlite
import json
from aiohttp import web
import aiopg
import random

pool = None


async def get_pool():
    global pool
    if pool is None:
        pool = await aiopg.create_pool(
            "dbname=test user=test password=test port=5432 host=127.0.0.1")
    return pool

max_n = 1000_000 - 1

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
