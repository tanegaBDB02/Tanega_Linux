#!/bin/bash

#setting the threshold percentage to 70
threshold=70

#checking the disk usage of the file system containing home directory
usage=$(df -P "$HOME" | awk 'NR==2 {print $5}' | sed 's/%//')

#checking if the disk usage is exceeding the threshold
if [ "$usage" -ge "$threshold" ]; then
    echo "Disk usage is at $usage%, which is above the $threshold% threshold"
else
    echo "Disk usage is at $usage%, which is under control"
fi
