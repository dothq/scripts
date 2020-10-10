#!/bin/sh

mkdir browser > /dev/null 2>&1
cd browser

git clone https://github.com/dothq/scripts tools && echo -e "\n\x1b[1;32mSUCCESS\x1b[0m Downloaded the build helper scripts.\n" || echo -e "\n\x1b[1;31mERROR\x1b[0m Failed to download build helper scripts.\n"