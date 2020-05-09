#!/usr/bin/env bash

uwsgi --http :8001 -w app_bottle:app --processes $PWPWORKERS
