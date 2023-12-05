#!/bin/bash

if [ "$#" -ne 2 ]; then 
    echo "Usage: $0 <day> <title>"
    exit 1
fi

cur_dir="$(dirname "$(readlink -f "$0")")"
template="$cur_dir/template.py"
base="$(echo "$cur_dir" | sed -e 's/utils//')"
cat $template | sed -e "s/DAY = -1/DAY = $1/" > "$base/$2.py"
test_dir="$base/inputs/day$1"
mkdir -p $test_dir
touch "$test_dir/test.txt"
touch "$test_dir/input.txt"
