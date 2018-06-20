if [[ -z $1 ]]; then
    echo "No process id provided." >&2
    exit 1
fi

pid=$1
data=$2
start=$(date "+%s")

if [[ -n $data ]]; then
    cat /dev/null >"$data"
fi

echo "Memory recorder started monitoring $1."

while [ 1 ]; do
    sleep 3
    res=$(ps ux -p $pid | tail -n 1 | sed -E 's/[[:space:]]+/,/g')

    if [[ $res == "" ]]; then
        break
    fi

    time=$(date "+%s")
    rel=$((time - start))

    if [[ -n $data ]]; then
        echo "$rel,$res" >>$data
    else
        echo "$rel,$res"
    fi
done

