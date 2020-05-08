from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import aiosqlite
from functools import lru_cache


async def get_conn():
    return await aiosqlite.connect("test.db")


async def homepage(request):
    conn = await get_conn()
    cursor = await conn.execute("select a, b from test")
    ((a, b),) = await cursor.fetchall()
    cursor.close()
    conn.close()
    return JSONResponse({"a": a, "b": b})


routes = [
    Route("/test", endpoint=homepage)
]


app = Starlette(routes=routes)
