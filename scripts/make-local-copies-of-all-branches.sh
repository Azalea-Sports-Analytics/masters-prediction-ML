#!/bin/sh

git fetch --all



for branch in $(git branch -r | grep -v '\->' | sed 's/origin\///'); do
    if git rev-parse --verify "$branch" >/dev/null 2>&1; then
        echo "Skipping $branch: already exists"
    else
        git switch --track "origin/$branch"
    fi
done
