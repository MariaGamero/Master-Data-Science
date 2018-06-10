######################################################################
#libraries
######################################################################
require(rvest)
require (xml2)
require(tidyverse)

######################################################################
#data loading
######################################################################
mundial <- read_html("https://es.wikipedia.org/wiki/Anexo:Tabla_estad%C3%ADstica_de_la_Copa_Mundial_de_F%C3%BAtbol",)

#La tabla estadistica de la Copa Mundial de Futbol presenta los datos de las 77 selecciones de futbol 
#que han participado en las 20 Copas Mundiales realizadas por la FIFA entre 1930 y 2014.
datos<- mundial %>% html_nodes("table") %>% .[[1]] %>% html_table()

######################################################################
#Quick review
######################################################################
str(datos)
head(datos)
summary(datos)

######################################################################
#Format
######################################################################
datos$Pos.=as.factor(datos$Pos.)
datos$Selección=as.factor(datos$Selección)
datos$Rend.=as.numeric(sub("%", "", datos$Rend.))/100
summary(datos)

######################################################################
#Query
######################################################################
datos %>% 

######################################################################
#Visualitation
######################################################################
datos %>% 





       
