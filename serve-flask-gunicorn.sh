#!/usr/bin/env bash

gunicorn -w $PWPWORKERS app_flask:app
