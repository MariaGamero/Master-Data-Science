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
names(mundialesGanados)<-c("Equipo","ID","Ganados","EdicionesGanadas")

#tabla3.- Tarjetas
tarjetas <- mundiales %>% html_nodes("table") %>% .[[5]] %>% html_table(header=TRUE)
names(tarjetas)<-c("Equipo","ID" ,"NumeroTarjetas" ,"TA", "2TA","TR","Ediciones","PartidosJugados" )


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
#Merge and remove
######################################################################

mundial<-merge(x = mundialesGanados[,c("ID","Ganados")], y =clasificacion , by = "ID", all.y = TRUE)
mundial<-merge(x = tarjetas[,c("ID","NumeroTarjetas","TA","2TA","TR","Ediciones")], y =mundial , by = "ID", all.y = TRUE)
head(mundial)

rm(clasificacion)
rm(mundialesGanados)
rm(tarjetas)
rm(mundiales)

######################################################################
#Quick review: mundial df
######################################################################

str(mundial)
head(mundial)
summary(mundial)

######################################################################
#Format
######################################################################
mundial$ID=as.factor(mundial$ID)
mundial$Equipo=as.factor(mundial$Equipo)
mundial$Ediciones=as.factor(mundial$Ediciones)

######################################################################
#Query
######################################################################
datosMundial<-mundial %>% 
  filter(!is.na(Ediciones)) %>% 
  mutate(Ganados=replace_na(Ganados, "0")) %>% 
  select(Equipo,Partic.,Ganados,Pts.,PJ,PG,PE,PP,GolesMarcados,GolesContra,PromedioPuntos.,NumeroTarjetas,TA,"2TA",TR,Ganados) %>% 
  arrange(desc(Pts.))

head(datosMundial)

######################################################################
#Visualitation
######################################################################
#gráfico 1
datosMundial %>% 
  filter(Ganados!= 0) %>% 
  ggplot(aes(x=Equipo,y=Partic.,color=Equipo,size=Ganados))+geom_point()+
  labs(x="Equipo", y="Participaciones")+ ggtitle("Detalle de mundiales por país")


#gráfico 2
ggplot(data=datosMundial,aes(x=Pts.,y=reorder(Equipo,Pts.),color=Pts.))+
  geom_point()+labs(x="Total puntos", y="Equipo")+
  ggtitle("Clasificación total puntos obtenidos en los mundiales 1973-2004")




       
