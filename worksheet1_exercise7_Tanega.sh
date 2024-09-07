#!/bin/bash

#hardcoding name of the input file
input_file="example.txt"

#check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "File '$input_file' not found!"
    exit 1
fi

#create a temporary file for the output
temp_file=$(mktemp)

#sorting the lines in the input file and remove duplicates
sort "$input_file" | uniq > "$temp_file"

#overwriting the original file with the deduplicated content
mv "$temp_file" "$input_file"

echo "Duplicate lines removed from '$input_file'"

