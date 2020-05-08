from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import aiopg

pool = None


async def get_pool():
    global pool
    if pool is None:
        pool = await aiopg.create_pool(
            "dbname=test user=test password=test port=5432 host=127.0.0.1")
    return pool

async def homepage(request):
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("select a, b from test")
            ((a, b),) = await cursor.fetchall()

    return JSONResponse({"a": a, "b": b})


routes = [
    Route("/test", endpoint=homepage)
]


app = Starlette(routes=routes)
