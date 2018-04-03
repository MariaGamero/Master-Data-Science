#!/bin/bash

echo "create a script that accepts a CSV filename as input (1$ inside your script) and returns the model of the aircraft with the higest number of engines. (use it on ~Data/opentraveldata/optd_aircraft.csv)"

#$1 = ~/Data/opentraveldata/optd_aircraft.csv 

csvgrep -d'^' -c nb_engines -r'[1-9]' $1 | csvsort -c7 -r | csvcut -c3,7 |csvlook | head


exit
