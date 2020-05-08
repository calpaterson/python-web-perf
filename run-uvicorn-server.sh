#!/usr/bin/env bash

uvicorn --port 8000 --workers $PWPWORKERS asgi_app:app
