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

mundiales <- read_html("https://es.fifa.com/fifa-tournaments/statistics-and-records/worldcup/teams/index.html")


#tabla1.- Clasificacion
clasificacion <- mundiales %>% html_nodes("table") %>% .[[2]] %>% html_table()
names(clasificacion)<-c("Nivel","Equipo","ID","Pts.","PJ","PG","PE","PP","GolesMarcados","GolesContra","PromedioPuntos.","Partic.")

#tabla2.- Mundiales ganados
mundialesGanados <- mundiales %>% html_nodes("table") %>% .[[1]] %>% 
  html_table(header=TRUE)
names(mundialesGanados)<-c("Equipo","ID","Ganados","EdicionesGanadas")

#tabla3.- Tarjetas
tarjetas <- mundiales %>% html_nodes("table") %>% .[[5]] %>% html_table(header=TRUE)
names(tarjetas)<-c("Equipo","ID" ,"NumeroTarjetas" ,"1TA", "2TA","TR","Ediciones","PartidosJugados" )


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
mundial<-merge(x = tarjetas[,c("ID","NumeroTarjetas","1TA","2TA","TR","Ediciones")], y =mundial , by = "ID", all.y = TRUE)
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
  select(Equipo,Partic.,Ganados,Pts.,PJ,PG,PE,PP,GolesMarcados,GolesContra,PromedioPuntos.,NumeroTarjetas,"1TA,"2TA",TR,Ganados) %>% 
  arrange(desc(Pts.))

head(datosMundial)

######################################################################
#Visualitation
######################################################################

#gráfico 1
tarjetas <- datosMundial %>% 
  select(Equipo,"1TA","2TA",TR)%>% 
  gather(clase,NumeroTarjetas,-Equipo) %>%  
  group_by(Equipo) %>% 
  arrange(Equipo) %>%
  ggplot(aes(x=clase,y=NumeroTarjetas,color=clase),size=3,alpha=.2,label=NumeroTarjetas)+
  geom_point(stat="identity")+facet_wrap(~Equipo)+labs(x="Tipo de Tarjeta",y= "Número de Tarjetas")+
  labs(title="Detalle del total tarjetas  por país",
       subtitle="Mundiales 1973-2004", 
       x="Tipo de Tarjeta")+ 
  scale_color_manual("clase",values=c("yellow1","orange1","red2"))+
  geom_text(aes(label=NumeroTarjetas),col="black",hjust=0, vjust=-1.5,size=3)+
  theme(axis.text.x = element_text(angle = 90,    #Roto 90° las etiquetas del eje x
                                   size = 6,      # Reduzco el tamaño a 6 puntos 
                                   color="blue"))+ #Cambio el color del texto a azul 
  theme(axis.text.y = element_text(size = 6,      
                                   color="blue"))


#gráfico 2
datosMundial %>% 
  filter(Ganados!= 0) %>% 
  ggplot(aes(x=Equipo,y=Partic.,color=Equipo,size=Ganados))+geom_point()+
  labs(x="Equipo", y="Participaciones")+ ggtitle("Detalle de mundiales por país")
  geom_text(aes(label=Ganados),col="black",hjust=2.5, vjust=.5,size=4)

#ggsave("ParticipaciónyMundialesGanadosPorPais.pdf", width = 18, height = 15, units = "cm")


#gráfico 3
ggplot(data=datosMundial,aes(x=Pts.,y=reorder(Equipo,Pts.),color=Pts.))+
  geom_point()+labs(x="Total puntos", y="Equipo")+
  ggtitle("Clasificación total puntos obtenidos en los mundiales 1973-2004")




       
