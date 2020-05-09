import bottle
import json

from sync_db import get_row

app = bottle.Bottle()

@app.route("/test")
def test():
    a, b = get_row()
    return json.dumps({"a": str(a).zfill(10), "b": b})
