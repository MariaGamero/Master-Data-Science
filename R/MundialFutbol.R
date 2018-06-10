#Análisis de la Copa Mundial de Futbol a partir de los datos de las 77 selecciones de futbol 
#que han participado en las 20 Copas Mundiales realizadas por la FIFA entre 1930 y 2014.

######################################################################
#libraries
######################################################################
require(rvest)
require (xml2)
require(tidyverse)

######################################################################
#data loading
######################################################################

#tabla1.- Clasificacion
clasificacion <- mundiales %>% html_nodes("table") %>% .[[2]] %>% html_table()
names(clasificacion)<-c("Nivel","Equipo","ID","Pts.","PJ","PG","PE","PP","GolesMarcados","GolesContra","PromedioPuntos.","Partic.")

#tabla2.- Mundiales ganados
mundialesGanados <- mundiales %>% html_nodes("table") %>% .[[1]] %>% 
  html_table(header=TRUE)
names(mundialesGanados)<-c("Equipo","ID","EdicionesGanadas","EdicionesGanadasAño")

#tabla3.- Tarjetas
tarjetas <- mundiales %>% html_nodes("table") %>% .[[5]] %>% html_table(header=TRUE)
names(tarjetas)<-c("Equipo","ID" ,"Total de tarjetas" ,"A", "2TA","TR","Ediciones","Partidos Jugados" )

######################################################################
#Quick review
######################################################################

str(clasificacion)
head(clasificacion)
summary(clasificacion)


str(mundialesGanados)     
head(mundialesGanados)    
summary(mundialesGanados)


str(tarjetas)
head(tarjetas)
summary(tarjetas)

######################################################################
#Format
######################################################################


######################################################################
#Query
######################################################################
datos %>% 

######################################################################
#Visualitation
######################################################################
datos %>% 





       
