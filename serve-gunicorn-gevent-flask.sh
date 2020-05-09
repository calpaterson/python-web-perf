#!/usr/bin/env bash

gunicorn -w $PWPWORKERS app_flask:app --worker-class gunicorn.workers.ggevent.GeventWorker
