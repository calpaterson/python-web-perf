#!/usr/bin/env bash

daphne -b 0.0.0.0 -p 8001 app_starlette:app
