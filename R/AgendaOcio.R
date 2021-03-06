####################################################################################
#Exercise: Conocer la distribucion en horas de los cursos realizados en Madrid
#y por Distritos 
####################################################################################

#Install Libraries..................................................................

library("dplyr")
library("data.table")
library("tidyr")

#Cargamos el fichero................................................................

agenda <- fread("DataR/agendaMadrid/2007.csv")

#Hacemos la consulta y al resultado lo denominamos AgendaOcioMadrid.................
agendaOcioMadrid<- agenda %>% 
  mutate(FECHA= as.Date(FECHA)) %>% 
  mutate(`FECHA-FIN` = as.Date(`FECHA-FIN`)) %>% 
  mutate(Duracion=(`FECHA-FIN`-FECHA))%>% 
  filter(Duracion>0, DISTRITO !="") %>% 
  group_by(DISTRITO,Duracion) %>% 
  summarise(TotalCursos=n(),HorasImpartidas=as.integer(sum(Duracion)))%>% 
  arrange(-HorasImpartidas)

#quitar outliers....................................................................
outliers<- boxplot.stats(agendaOcioMadrid$HorasImpartidas)$out
length(outliers)
outliers

#Creamos una nueva variable:agendaOcioMadrid_SinOutliers
agendaOcioMad_SinOutliers <- agendaOcioMadrid %>% 
  filter(!HorasImpartidas %in% outliers) 

#borramos el data anterior 
rm(agendaOcioMadrid)

#Graficamente.........................................................................
library(ggmap)
library(tidyverse)
library(ggplot2)

spread(agendaOcioMad_SinOutliers)
table(agendaOcioMad_SinOutliers$HorasImpartidas)

#vamos a hacer tranchas para las horas:
gr.horas=cut(agendaOcioMad_SinOutliers$HorasImpartidas,breaks=seq(0,60,10))

agendaOcioMad_SinOutliers<-as.tibble(agendaOcioMad_SinOutliers) %>% mutate(media=mean(Duracion))
qplot(gr.horas,reorder(DISTRITO, media),data=agendaOcioMad_SinOutliers, geom=c("point","smooth"),xlab="Horas",ylab="Distrito")
  
