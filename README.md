# Python webserver performance comparison

This repository holds some benchmarking configuration for a number of popular
python webserver configurations:

- nginx and aiohttp
- nginx, gunicorn and flask
- nginx, uvicorn and starlette
- nginx, uwsgi and flask

These are benchmarked by apache-bench.

The nginx configuration is included, which listens on port 8001.

The servers are run from shell scripts.

## $PWPWORKERS

This variable controls how many workers are started.  Most of the async servers
don't benefit from many more workers than cores available.  Most of the sync
workers do benefit from this though (often 2*`nproc`) is a good starting point.

Except for Daphne - see below.

## Daphne

Daphne doesn't have a front facing proxy and so requires nginx to do the load
balancing.  Not a bad idea but means that to test it you need to edit nginx's
conf and start multiple instances.

https://github.com/django/daphne/issues/79#issuecomment-278188287

## Slow ttys

Some terminals are quite slow, for example gnome-terminal.  Many of the wsgi
servers output an access log to either stdout and stderr (uwsgi, daphne and
uvicorn) - that needs to be redirected to a `/dev/null` to ensure a fair
comparison.

## Getting set up on Mac

### Set up the virtualenv

```bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements_frozen.txt
```

### Create the db and populate

```bash
psql postgres -c 'CREATE DATABASE test'
psql test < schema.sql
psql test -c "CREATE USER test WITH PASSWORD 'test'"
psql test -c "GRANT SELECT ON ALL TABLES IN SCHEMA public TO test"
python gen_test_data.py | psql test -c 'COPY test FROM STDIN CSV HEADER'
pgbouncer -d pgbouncer.ini
# test it works with
psql postgres://test:test@localhost:6432/test -c 'SELECT * FROM test LIMIT 10'
```

### Run a server

```bash
PWPWORKERS=4 ./serve-gunicorn-flask.sh
```

### Test

```bash
./run-benchmark.sh > runs/gunicorn-flask.txt
```

## Outcomes

In `/runs`
