#!/usr/bin/env bash

gunicorn --bind :8001 -w $PWPWORKERS app_bottle:app --worker-class "egg:meinheld#gunicorn_worker"
