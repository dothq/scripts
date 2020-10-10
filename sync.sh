#!/bin/sh

cd browser/dot
find . -name '*' -exec cp -r --parents \{\} ../firefox \;