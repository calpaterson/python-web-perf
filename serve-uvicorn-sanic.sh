#!/usr/bin/env bash

uvicorn --port 8000 --workers $PWPWORKERS app_sanic:app
