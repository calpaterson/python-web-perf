#!/usr/bin/env bash

gunicorn -w $PWPWORKERS app:app --worker-class gunicorn.workers.ggevent.GeventWorker
