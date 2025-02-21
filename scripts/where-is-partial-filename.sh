#!/bin/sh

# Check if a search term is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <partial_filename>"
    exit 1
fi

SEARCH_TERM=$1

# Loop through all remote branches
for branch in $(git branch -r |  fgrep -v -e  '->' | sed 's/origin\///'); do
    # List files in the branch and search for the partial match (case insensitive)
    if git ls-tree -r origin/$branch --name-only | grep -i "$SEARCH_TERM" >/dev/null; then
        echo "$branch contains files matching '$SEARCH_TERM'"
    fi
done
