#!/usr/bin/env bash

dir="$(dirname $0)"
pid=$1
start=$(date "+%s")
drawpid=0
watchpid=0

trap stop INT

if [[ -z $pid ]]; then
    echo "Error: No process ID provided." >&2
    exit 1
fi

function stop {
    echo "Stopping"
    kill $drawpid $watchpid
}

function plot_memory_usage {
    while :; do
        python "$dir/plot_memory_usage.py" "$dir/data/${pid}.txt" "$dir/${pid}_memory_usage.png"
        sleep 5
    done
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

plot_memory_usage &
watchpid=$!

record_memory_usage &
drawpid=$!

echo "Started recorder ($watchpid) and plotter ($drawpid)"

sleep 1
open "$dir/images/${pid}_memory_usage.png"

wait

