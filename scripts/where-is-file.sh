#!/bin/sh

# Check if a filename is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

FILENAME=$1

# Loop through all remote branches
for branch in $(git branch -r | sed 's/origin\///'); do
    if git ls-tree -r origin/$branch -- "$FILENAME" &>/dev/null; then
        echo "$branch contains $FILENAME"
    fi
done
