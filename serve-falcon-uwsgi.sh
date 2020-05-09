#!/usr/bin/env bash

uwsgi --http :8000 -w app_falcon:app --processes $PWPWORKERS
