#!/usr/bin/env bash

CONCURRENCY=100
REQUEST_COUNT=10000

ab -c $CONCURRENCY -n $REQUEST_COUNT http://localhost:8001/test
