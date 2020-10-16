#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

throw() {
    payload="$1"

    echo -e "\n$payload\n"
    exit 1;
}

info() {
    payload="$1"

    echo -e "\n\x1b[1;34mINFO\x1b[0m $payload\n"
}

start_py() {
    py_bin="$1"

    if which $py_bin > /dev/null 2>&1
    then
        info "This script is WIP"
        info "Syncing..."
        exec $py_bin "$DIR/sync.py"
    else
        throw "You will need '$py_bin' installed for this script to run."
    fi
}

start_py python3