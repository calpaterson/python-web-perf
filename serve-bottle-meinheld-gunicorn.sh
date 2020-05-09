#!/usr/bin/env bash

gunicorn -w $PWPWORKERS app_bottle:app --worker-class "egg:meinheld#gunicorn_worker"
