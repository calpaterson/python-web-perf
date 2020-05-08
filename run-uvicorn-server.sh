#!/usr/bin/env bash

uvicorn --port 8000 --workers `nproc` asgi_app:app
