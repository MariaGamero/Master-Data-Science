#!\bin\bash

#Create database from shell
createdb db_exercise_opentraveldata

#import tables from ~/Data/opentraveldata

csvsql -d'^' ~/Data/opentraveldata/ref_airline_nb_of_flights.csv | psql db_exercise_opentraveldata
csvsql -d'^' ~/Data/opentraveldata/optd_airlines.csv | psql db_exercise_opentraveldata

exit
