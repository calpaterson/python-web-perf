import flask


app = flask.Flask("gunicorn-perf")


@app.route("/test")
def test():
    return "ok"
