#!/usr/bin/env bash

gunicorn -w $PWPWORKERS app_flask:app --worker-class "egg:meinheld#gunicorn_worker"
