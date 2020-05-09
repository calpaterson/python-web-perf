import flask
import json
import random
from sync_db import get_row

app = flask.Flask("python-web-perf")

pool = None

@app.route("/test")
def test():
    a, b = get_row()
    return json.dumps({"a": str(a).zfill(10), "b": b})
