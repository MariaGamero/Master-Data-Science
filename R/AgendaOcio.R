#####################################################################
#Install Libraries
#####################################################################

list.of.packages <- c("R.utils", "tidyverse", "doParallel", "foreach", "sqldf", "broom", "DBI", "ggplot2", "tidyr", "lubridate")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

library("dplyr")
library("data.table")
library("tidyr")


agenda <- fread("data/agendaMadrid/2007.csv")
class(agenda)

agenda %>% 
  mutate(FECHA= as.Date(FECHA)) %>% 
  mutate(`FECHA-FIN` = as.Date(`FECHA-FIN`)) %>% 
  mutate(duracionDias=(`FECHA-FIN`-FECHA))%>% 
  separate(FECHA, c("COMIENZO","day","hour"),c(7,9)) %>%
  filter(duracionDias>0,!is.na(DISTRITO)) %>% 
  select(COMIENZO,`TITULO-ACTIVIDAD`,`DIAS-SEMANA`,DISTRITO,duracionDias,GRATUITO) %>% 
  group_by(DISTRITO) %>%
  arrange(-duracionDias)


