#!/usr/bin/env bash

uwsgi --http :8000 -w app:app --processes 8
