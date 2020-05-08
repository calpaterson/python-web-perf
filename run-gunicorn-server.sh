#!/usr/bin/env bash

gunicorn -w $PWPWORKERS app:app
