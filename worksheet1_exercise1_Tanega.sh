#!/bin/bash

#finding the directory where to search for the executable files 
dir="$HOME"
#to list all executable files in that directory
for file in "$dir"/*
do
if [ -x "$file" ] && [ -f "$file" ]
then
echo "$file"
fi
done





