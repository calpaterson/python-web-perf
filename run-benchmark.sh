#!/usr/bin/env bash

CONCURRENCY=100

ab -c $CONCURRENCY -n 10000 http://localhost:8001/test
