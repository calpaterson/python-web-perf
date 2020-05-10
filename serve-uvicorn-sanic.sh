#!/usr/bin/env bash

uvicorn --port 8001 --workers $PWPWORKERS app_sanic:app
