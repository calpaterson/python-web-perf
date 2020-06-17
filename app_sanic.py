from os import environ

from sanic import Sanic
from sanic.response import json

from async_db import get_row

app = Sanic("python-web-perf")


@app.route("/test")
async def test(request):
    a, b = await get_row()
    return json({"a": str(a).zfill(10), "b": b})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, workers=int(environ["PWPWORKERS"]))
