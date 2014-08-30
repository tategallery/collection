#!/bin/bash

mkdir images0

IFS=,
base=http://www.tate.org.uk/art/images/work/

# the csv with only acno and unique part of url, should be pre-processed to get rid of url-less rows
csv=../processed/simplified_artwork_data.csv

echo -e "Which line in the csv should I go to: \c"
read number
echo "The script will start at line: $number"

# go to the number of the line requested
# download the thumbnail associated with the image
# with the name of the acno
awk 'NR>$number' $csv | while read a1 a2
do
	echo $a1
	URL=$base$a2
	curl -o images0/$a1.jpg $URL
done

# csv2=../processed/ar_only_no_empty.csv
# awk 'NR>470' $csv2 | while read a1 a2
# do
# 	echo $a1
# 	URL=$base$a2
# 	curl -o images0/ar/_large/$a1.jpg $URL
# done