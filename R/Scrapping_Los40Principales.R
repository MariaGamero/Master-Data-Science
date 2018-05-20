install.packages("stringr")
library("stringr")

url<-"http://los40.com/lista40/?o=VL40"

readLines(url)

htmlLines <- readLines(url)
htmlCode <- paste(htmlLines, collapse = "")

artistName <- "\\d.'nombre_artista']\\s{3}=\\s'(.*?)';"

artistList <- str_match_all(htmlCode,artistName)[[1]][,2]
