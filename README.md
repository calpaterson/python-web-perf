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

There is a makefile which runs a full build.
