#!/usr/bin/env bash

gunicorn -w $PWPWORKERS app:app --worker-class "egg:meinheld#gunicorn_worker"
