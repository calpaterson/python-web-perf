#!/usr/bin/env bash

uwsgi --uwsgi-socket :8001 -w app_bottle:app --processes $PWPWORKERS
