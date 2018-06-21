#!/usr/bin/env bash

dir="$(cd "$(dirname $0)" && pwd)"
install=0

while [[ $# -gt 0 ]]; do
    case $1 in
        --install|-i) install=1;;
        *) echo "Unknown argument provided: $1" >&2; exit 1;;
    esac

    shift
done

if [[ $install -ne 0 ]]; then
    pip install -r "$dir/requirements.txt"
fi

FLASK_APP="$dir/statistics_server" FLASK_DEBUG=1 python -m flask run

