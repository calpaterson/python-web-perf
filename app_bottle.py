import bottle
import json

from sync_db import get_row

app = bottle.Bottle()


@app.route("/test")
def test():
    a, b = get_row()
    return json.dumps({"a": str(a).zfill(10), "b": b})


@app.route("/test2")
def test2():
    a, b = get_row()
    x, y = get_row()
    z, w = get_row()
    return json.dumps(
        {
            "a": str(a).zfill(10),
            "b": b,
            "x": str(x).zfill(10),
            "y": y,
            "z": str(z).zfill(10),
            "w": w,
        }
    )
