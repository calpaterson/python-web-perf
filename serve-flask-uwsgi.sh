#!/usr/bin/env bash

uwsgi --http :8000 -w app_flask:app --processes $PWPWORKERS
