import flask
import psycopg2
import psycopg2.pool
from functools import lru_cache
import json
import random

app = flask.Flask("gunicorn-perf")

pool = None

def get_pool():
    global pool
    if pool is None:
        pool = psycopg2.pool.SimpleConnectionPool(
            1, 3, database="test", user="test", password="test", port=6432,
        )
    return pool


max_n = 1000_000 - 1


def get_row():
    conn = get_pool().getconn()
    cursor = conn.cursor()
    index = random.randint(1, max_n)
    cursor.execute("select a, b from test where a = %s;", (index,))
    ((a, b),) = cursor.fetchall()
    cursor.close()
    get_pool().putconn(conn)
    return a, b


@app.route("/test")
def test():
    a, b = get_row()
    return json.dumps({"a": a, "b": b})
