#The goal with this exercise is to scrape a website in order to
#extract LOS 40 stations broadcast in Spain (List of Artists).

#On this ocassion I will use the string package. 
install.packages("stringr")
library("stringr")

url<-"http://los40.com/lista40/?o=VL40"
#readLines(url)


htmlLines <- readLines(url)
htmlCode <- paste(htmlLines, collapse = "")

#For regular expressions I will use: https://regex101.com/

artistName <- "\\d.'nombre_artista']\\s{3}=\\s'(.*?)';"

#Finally, I will extract matched groups (astistName) from a string (htmlCode), to get a list of character matrices. 
# First column is the complete match, followed by one column for the capture group (artistName). 

artistList <- str_match_all(htmlCode,artistName)[[1]][,2]
