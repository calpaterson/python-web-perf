#!/usr/bin/env bash

CONCURRENCY=100
REQUEST_COUNT=100000

ab -c $CONCURRENCY -n $REQUEST_COUNT http://localhost:8000/test
