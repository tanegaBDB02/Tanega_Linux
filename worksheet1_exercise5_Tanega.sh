#!/bin/bash

#getting the total space for the root filesystem 
total_root=$(df / | awk 'NR==2 {print $2}')

#getting the used space for the home filesystem
home_used=$(df "$HOME" | awk 'NR==2 {print $3}')

    #calculating the percentage as an approximate number
    percentage=$((100 * $home_used / $total_root))
    echo "$HOME directory is using approximately $percentage% of the total space of the root directory"
