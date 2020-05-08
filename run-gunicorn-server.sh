#!/usr/bin/env bash

gunicorn -w `nproc` app:app
