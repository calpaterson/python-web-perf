#!/usr/bin/env bash

gunicorn aio_app:app -w 8 --bind localhost:8000 --worker-class aiohttp.GunicornWebWorker
