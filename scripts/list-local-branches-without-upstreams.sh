#!/bin/sh

git fetch --prune
git branch -vv | awk '/origin\/.+: gone]/ {print $1}'
