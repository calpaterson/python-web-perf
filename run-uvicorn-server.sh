#!/usr/bin/env bash

uvicorn --port 8000 --workers `nproc` async_app:app
