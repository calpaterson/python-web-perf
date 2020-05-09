#!/usr/bin/env bash

gunicorn aio_app:app -w $PWPWORKERS --bind localhost:8000 --worker-class aiohttp.GunicornWebWorker
