#!/usr/bin/env bash

uwsgi --http-socket :8001 -w app_falcon:app --processes $PWPWORKERS
