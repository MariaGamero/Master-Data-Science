
library(readr)

#flights <- read.csv('data/flights/2008.csv')

#install.packages((dplyr))
library(dplyr)

##########################################################################
# Exercises: 
# 1) Keep flights that are delayed (ArrDelay > 0 and not NA). 
# Next, create a by-carrier summary with a single variable: avg, the average delay 
# of the delayed flights. Again add a new variable rank to the summary according to 
# avg. Finally, arrange by this rank variable.


flights %>% 
  filter(!is.na(ArrDelay)) %>% 
  group_by(UniqueCarrier) %>% 
  summarise(avg=mean(ArrDelay >0)) %>% 
  mutate(rank = rank(avg)) %>% 
  arrange(rank)


# 2) How many airplanes only flew to one destination from JFK? 
# The result contains only a single column named nplanes and a single row.

flights %>% 
  mutate(nplanes=(Dest == "JKF")) %>% 
  summarise(nplanes=n())


# 3) Find the most visited destination for each carrier
# Your solution should contain four columns:
# UniqueCarrier and Dest, n, how often a carrier visited a particular destination,
# rank, how each destination ranks per carrier. rank should be 1 for every row, 
# as you want to find the most visited destination for each carrier.

flights %>% 
  group_by(UniqueCarrier,Dest) %>%
  summarise(n=n()) %>% 
  mutate(rank = rank(n)) %>% 
  arrange(rank)