#!/bin/bash

#setting the threshold value
threshold=90

#looping through numbers 1 to 100
for number in {1..100}; do
    #print the number
    echo "Number: $number"
    
    #checking if the number is greater than the threshold
    if [ "$number" -gt "$threshold" ]; then
        echo "$number is greater than the threshold $threshold"
    fi
done

