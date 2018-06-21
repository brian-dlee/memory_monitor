#!/usr/bin/env bash

dir="$(dirname $0)"
pid=$1
start=$(date "+%s")
watchpid=0

trap stop INT

if [[ -z $pid ]]; then
    echo "Error: No process ID provided." >&2
    exit 1
fi

function stop {
    echo "Stopping"
    kill $watchpid
}

function record_memory_usage {
    cat /dev/null >"$dir/data/${pid}.txt"

    while :; do
        res=$(ps ux -p $pid | tail -n 1 | sed -E 's/[[:space:]]+/,/g')

        if [[ $res == "" ]]; then
            break
        fi

        time=$(date "+%s")
        rel=$((time - start))

        echo "$rel,$res" >>"$dir/data/${pid}.txt"
        sleep 3
    done
}

record_memory_usage &
watchpid=$!

echo "Started recorder ($watchpid)"

wait

