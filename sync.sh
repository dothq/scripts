#!/bin/sh

cd browser/dot

copy() {
    echo "Syncing $1..."
    \cp -r "$1" "../firefox/$1"
}

for f in $(find . -not \( -path ./.git -prune \) -not \( -path ./.hg -prune \) -name '*'); do copy $f; done