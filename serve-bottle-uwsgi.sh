#!/usr/bin/env bash

uwsgi --http :8000 -w app_bottle:app --processes $PWPWORKERS
