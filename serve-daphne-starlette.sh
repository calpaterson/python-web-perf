#!/usr/bin/env bash

daphne -b 0.0.0.0 -p 8000 app_starlette:app
