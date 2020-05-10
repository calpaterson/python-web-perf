#!/usr/bin/env bash

uwsgi --http-socket :8001 -w app_flask:app --processes $PWPWORKERS
