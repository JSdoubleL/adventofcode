#!/bin/bash

if [ "$#" -ne 3 ]; then 
    echo "Usage: $0 <year> <day> <title>"
    exit 1
fi

new_dir="$1/day$2"

cd "$(dirname "$(readlink -f "$0")")"
mkdir -p $new_dir
cp "template.py" "$new_dir/$3.py"
touch "$new_dir/test.txt"
touch "$new_dir/input.txt"
