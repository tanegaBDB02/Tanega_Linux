#!/bin/bash

#extracting the current time
current_time=$(date +"%H")

#determining the appropriate greeting based on the current time
if [ "$current_time" -ge 5 ] && [ "$current_time" -lt 12 ]
then
    echo "Good morning!"
elif [ "$current_time" -ge 12 ] && [ "$current_time" -lt 18 ]
then
    echo "Good afternoon!"
else
    echo "Good night!"
fi
