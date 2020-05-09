#!/usr/bin/env bash

gunicorn aio_app:app -w $PWPWORKERS --bind localhost:8001 --worker-class aiohttp.GunicornWebWorker
