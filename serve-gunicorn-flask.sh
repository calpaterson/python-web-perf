#!/usr/bin/env bash

gunicorn -w $PWPWORKERS --bind :8001 app_flask:app
