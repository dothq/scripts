#!/bin/sh

mkdir browser > /dev/null 2>&1
cd browser

post_git_clone() {
    echo -e "\n\x1b[1;32mSUCCESS\x1b[0m Downloaded the build helper scripts.\n"

    # remove self
    rm $(pwd)/tools/download-scripts.sh
}

git clone https://github.com/dothq/scripts tools && post_git_clone || echo -e "\n\x1b[1;31mERROR\x1b[0m Failed to download build helper scripts.\n"