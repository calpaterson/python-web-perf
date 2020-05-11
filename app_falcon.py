import falcon
import json

from sync_db import get_row


class ThingResource:
    def on_get(self, req, resp):
        a, b = get_row()
        resp.body = json.dumps({"a": str(a).zfill(10), "b": b})

app = falcon.API()

things = ThingResource()

app.add_route("/test", things)
