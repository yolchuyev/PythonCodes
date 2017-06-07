#!/bin/bash
path="$1"

while IFS='' read -r directory || [[ -n "$directory" ]]; do
    if [ -d "$path/$directory" ]; then
      printf "[+] Directory $path/$directory exists!\n"
    fi
done < "$2"
