#!/usr/bin/env bash

gunicorn -k uvicorn.workers.UvicornWorker -w $PWPWORKERS --bind :8001 app_fastapi:app
