import aiosqlite
import json
from aiohttp import web


async def get_conn():
    return await aiosqlite.connect("test.db")


async def handle(request):
    conn = await get_conn()
    cursor = await conn.execute("select a, b from test")
    ((a, b),) = await cursor.fetchall()
    cursor.close()
    conn.close()
    return web.Response(text=json.dumps({"a": a, "b": b}))


app = web.Application()
app.add_routes([web.get('/test', handle)])


if __name__ == '__main__':
    web.run_app(app)
