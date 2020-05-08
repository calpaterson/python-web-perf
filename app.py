import flask
import sqlite3
from functools import lru_cache
import json


app = flask.Flask("gunicorn-perf")


def get_conn():
    return sqlite3.connect("test.db")


def get_row():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("select a, b from test")
    ((a, b),) = cursor.fetchall()
    cursor.close()
    conn.close()
    return a, b


@app.route("/test")
def test():
    a, b = get_row()
    return json.dumps({"a": a, "b": b})
