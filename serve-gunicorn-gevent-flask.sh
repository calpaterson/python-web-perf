#!/usr/bin/env bash

gunicorn --bind :8001 -w $PWPWORKERS app_flask:app --worker-class gunicorn.workers.ggevent.GeventWorker
