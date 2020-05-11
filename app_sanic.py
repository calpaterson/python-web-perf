from sanic import Sanic
from sanic.response import json

from async_db import get_row

app = Sanic("python-web-perf")


@app.route("/test")
async def test(request):
    # a, b = await get_row()
    # return json({"a": str(a).zfill(10), "b": b})

    # Add some complexity to this baby, so async can shine.
    # Tried using pokeapi.co API, but got banned after a few tests.
    # 3 queries should be enough to prove a point.
    a, b = await get_row()
    x, y = await get_row()
    z, w = await get_row()
    return json(
        {
            "a": str(a).zfill(10),
            "b": b,
            "x": str(x).zfill(10),
            "y": y,
            "z": str(z).zfill(10),
            "w": w,
        }
    )
