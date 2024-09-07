#!/bin/bash
dir="source"
file="empty_folders.txt"
if [ ! -d "$dir" ]; then
    echo "Error: Directory $dir does not exist"
    exit 1
fi
find "$dir" -type d -empty > "$file"
echo "Empty subdirectories have been listed in $file"
