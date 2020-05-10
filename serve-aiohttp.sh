#!/usr/bin/env bash

gunicorn app_aio:app -w $PWPWORKERS --bind localhost:8001 --worker-class aiohttp.GunicornWebWorker
