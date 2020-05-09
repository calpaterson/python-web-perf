#!/usr/bin/env bash

gunicorn -w $PWPWORKERS app_falcon:app --worker-class "egg:meinheld#gunicorn_worker"
