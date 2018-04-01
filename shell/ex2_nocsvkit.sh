#!/bin/bash

echo "QUICK EXERCISES SIN USAR CSVKIT"
echo "Hoy es 'date'"

# Go to ~/Data/opentraveldata

echo "1. Use grep to extract al 7x7 or 3xx (where x can be any number) airplane models from optd_aircraft.csv"
cat ~/Data/opentraveldata/optd_aircraft.csv | cut -d '^' -f3 | grep '^3' | uniq -c
cat ~/Data/opentraveldata/optd_aircraft.csv | cut -d '^' -f3 | grep '^7' | grep -E '[%7]'

echo "2. Use grep to obtain the number of airlines with prefix 'areo'in their name from optd_airlines.csv"
cat ~/Data/opentraveldata/optd_airlines.csv | cut -d '^' -f8,9 | grep '^[a|A]ero' |sort |uniq -c |wc -l

echo "3. How many optd_por_public.csv columns have 'name' as part of their name? What are the numerical positions?(hint:use seq and paste)"

echo "the number of columns is: " 
head -1 ~/Data/opentraveldata/optd_por_public.csv | tr '^' '\n'|grep 'name' | uniq -c | wc -l

echo "Their numerical positions are: "
seq 1 `head -1 ~/Data/opentraveldata/optd_por_public.csv | tr '^' '\n' | wc -l`> ~/nums.txt

head -1 ~/Data/opentraveldata/optd_por_public.csv | tr '^' '\n'| uniq > ~/columns.txt

paste ~/nums.txt ~/columns.txt | grep 'name'




exit

