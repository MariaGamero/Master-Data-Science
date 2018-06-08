require(rvest)
require (xml2)
require(tidyverse)

mundial <- read_html("https://es.wikipedia.org/wiki/Anexo:Tabla_estad%C3%ADstica_de_la_Copa_Mundial_de_F%C3%BAtbol",)
#La tabla estadistica de la Copa Mundial de Futbol presenta los datos de las 77 selecciones de futbol 
#que han participado en las 20 Copas Mundiales realizadas por la FIFA entre 1930 y 2014.

simbologia<- mundial %>% 
  html_nodes("div") %>% .[[14]]%>% html_text(trim=TRUE) %>% strsplit("\n")
simbologia[[1]][-9]

datos<- mundial %>% 
  html_nodes("table") %>% .[[1]] %>% html_table()

datos %>% 
  ggplot(aes(x=Rend., y=Selección,color=Ediciones))+geom_point()

datos<- datos %>% group_by(Selección) %>% mutate(media=mean(Pts.))
qplot(Pts.,reorder(Selección, media),col=Selección)       
       