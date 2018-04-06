#!/bin/bash

## step1_Create database from shell

#createdb db_exercise_opentraveldata

## step2_Import tables from ~/Data/opentraveldata

#csvsql -d'^' ~/Data/opentraveldata/ref_airline_nb_of_flights.csv | psql db_exercise_opentraveldata
#csvsql -d'^' ~/Data/opentraveldata/optd_airlines.csv | psql db_exercise_opentraveldata

## step3_Import data

#\copy ref_airline_nb_of_flights from '~/Data/opentraveldata/ref_airline_nb_of_flights.csv' delimiter '^' csv header
#\copy ref_airline_nb_of_flights from '~/Data/opentraveldata/ref_airline_nb_of_flights.csv' delimiter '^' csv header

#step4_query:

select * from ref_airline_nb_of_flights as l 
left outer join (select "2char_code",name as airline_name from optd_airlines group by "2char_code",name) as r 
on l.airline_code_2c=r."2char_code";


exit
