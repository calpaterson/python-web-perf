import flask
import json
from sync_db import get_row

app = flask.Flask("python-web-perf")

pool = None


@app.route("/test")
def test():
    # a, b = get_row()
    # return json.dumps({"a": str(a).zfill(10), "b": b})
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
