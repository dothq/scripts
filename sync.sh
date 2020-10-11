#!/bin/sh

cd $(pwd)/dot

copy() {
    echo "Syncing $1..."

    echo [ -d "$1" ]
}

for f in $(find . -not \( -path ./.git -prune \) -not \( -path ./.hg -prune \) -name '*'); do copy $f; done