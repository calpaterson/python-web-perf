## Test config

Benchmarked on MacBook with PWPWORKERS=2.
Dockerized PostgreSQL (see `docker-compose.yaml` file).
No nginx.
Flask vs Sanic

2 scenarios:

1. 1 db query
2. 3 db queries


## Outcomes

1. `runs-tudor` baseline tests, with the same .py files as Cal's, but on my Mac.
2. `runs-tudor-non-trivial-requests` containt outputs for .py files with 3 db queries. The core of this bechmark.
Sanic handled >3x more requests and a lot lower time per request than Flask.


## Other

- flask app transfers more data over the wire than the sanic app
  - no compression. That's fine for a benchmark.
- sanic app has the right content-type headers set (might not matter)
- worth checking https://github.com/vibora-io/vibora too