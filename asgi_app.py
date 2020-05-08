from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
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

async def homepage(request):
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            index = random.randint(1, max_n)
            await cursor.execute("select a, b from test where a = %s", (index,))
            ((a, b),) = await cursor.fetchall()

    return JSONResponse({"a": str(a).zfill(10), "b": b})


routes = [
    Route("/test", endpoint=homepage)
]


app = Starlette(routes=routes)
