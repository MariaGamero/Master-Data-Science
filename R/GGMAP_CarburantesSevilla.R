
#Importamos libraries#####################################################################
install.packages("plotly")
install.packages("tmap")
require(ggmap)
require(ggplot2)
library(tidyverse)
library(tidytext)
##########################################################################################


#Pintar las gasolineras en el mapa de la provincia de Sevilla utilizando 
#el fichero data/carburantes.csv 
#Modificar el tamaño (o color) de los puntos en función de, por ejemplo, el precio de los carburantes.

seville<-geocode('Seville')
seville<-c(lon=-5.984459,lat=37.38909)
sevilleMap <- ggmap(get_map(seville, zoom=10,color = "bw"))
sevilleMap

#Cargamos la BD y filtramos por provincia de Sevilla (esto no hace falta)
carburantes<- read.csv2("data/carburantes.csv")
carburantesSevilla<- carburantes %>% filter(Provincia %in% c("SEVILLA") &!is.na(Precio.Gasoleo.A) & !is.na(Precio.Gasolina.95.ProtecciÃ³n))

#Plot
sevilleMap + 
  geom_point(data=carburantesSevilla,aes(x=Longitud..WGS84.,y=Latitud..WGS84.,color=Precio.Gasoleo.A,size=Precio.Gasolina.95.ProtecciÃ³n) 
             ,alpha=.3)+
  ggtitle("Gasolineras en Sevilla")+labs(x="longitud",y="latitud", color = "Precio del gasoil", size="Pº Gasolina")

#Saving the plot
ggsave("carburantesSevilla.pdf",width=8,height=12)
