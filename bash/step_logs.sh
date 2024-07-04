#!/usr/bin/env bash
BRANCH="master"

#This was writen based on a course on LinkedIn learning with some minor adjustments.

# Save the current time into a log file
echo "Current Date:" >> ./code/bash/log.txt && date '+%Y-%m-%d' >> ./code/bash/log.txt
echo "Current Time:" >> ./code/bash/log.txt && date '+%r' >> ./code/bash/log.txt
echo "Epoch Time:" >> ./code/bash/log.txt && date '+%s' >> ./code/bash/log.txt
echo " " >> ./code/bash/log.txt

# Commit
p=$(pwd)
git config --global --add safe.directory $p

if [[ "$(git status --porcelain)" != "" ]]; then
    git config --global user.name $USER_NAME
    git config --global user.email $USER_EMAIL
    git add code/bash/log.txt
    git commit -m "Update the log"
    git push origin $BRANCH
else
echo "Nothing to commit..."
fi
