#!/usr/bin/env bash

gunicorn -w 8 app:app
