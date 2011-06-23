#!/bin/bash
BW=0
COLOR=0
file="$1"

for page in $(identify -density 12 -format '%p ' "$file") ; do
    if convert "$file[$((page-1))]" -colorspace RGB -unique-colors txt:- | sed -e 1d | egrep -q -v ': \(\s*([0-9]*),\s*\1,\s*\1' ; then
        echo $page
	let COLOR=COLOR+1
    else
	let BW=BW+1
    fi
done

echo "Total B/W Pages: $BW"
echo "Total Color Pages: $COLOR"
