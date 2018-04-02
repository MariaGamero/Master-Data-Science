#!/bin/bash

echo "QUICK EXERCISES USANDO CSVKIT"
echo "Hoy es 'date'"

# Go to ~/Data/opentraveldata

echo "1. Use grep to extract al 7x7 or 3xx (where x can be any number) airplane models from optd_aircraft.csv"

csvgrep -d '^' -c model -r'^7.7|^3' ~/Data/opentraveldata/optd_aircraft.csv | csvlook

echo "2. Use grep to obtain the number of airlines with prefix 'areo'in their name from optd_airlines.csv"


csvgrep -d '^' -c name -r'^[a|A]ero' ~/Data/opentraveldata/optd_airlines.csv | wc -l


echo "3. How many optd_por_public.csv columns have 'name' as part of their name? What are the numerical positions?(hint:use seq and paste)"

exit
