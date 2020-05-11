import json
from aiohttp import web
import aiopg

from async_db import get_row

async def handle(request):
    a, b = await get_row()
    return web.Response(text=json.dumps({"a": str(a).zfill(10), "b": b}))


app = web.Application()
app.add_routes([web.get('/test', handle)])
