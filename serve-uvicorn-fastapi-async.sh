#!/usr/bin/env bash

uvicorn --port 8001 --workers $PWPWORKERS app_fastapi_async:app --log-level error
