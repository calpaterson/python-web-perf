#!/usr/bin/env bash -x

CONCURRENCY=100
REQUEST_COUNT=10000

SERVERS=("uvicorn-sanic" "gunicorn-flask")
ENDPOINT="/test2"
OUTPUT_DIR="runs-tudor-with-non-trivial-requests"

for SERVER in "${SERVERS[@]}"
do

# Start the server
PWPWORKERS=4 ./serve-"${SERVER}".sh > /dev/null 2>/dev/null &

# random time. Figure out a more reliable way.
sleep 5

# obtain pid of main proc
LAST_PID=$(ps | grep "/Applications/Xcode.app/Contents" | awk 'NR==1{split($0, a); print a[1]}')

ab \
-c $CONCURRENCY \
-n $REQUEST_COUNT "http://127.0.0.1:8001${ENDPOINT}" > "${OUTPUT_DIR}"/"${SERVER}".txt 

# kill the main proc
kill $LAST_PID

done
