#leer los datos
titanic <- read.csv("train.csv")

#EJERCICIOS R

#Cúal es la edad del sujeto número 7
titanic[7,"Age"]
  
#Obtener el sujeto 7  
titanic[7,]

# Segundo ejercicio. Que edad tiene la persona más joven
min(titanic$Age, na.rm = T)

#Calcula la media y mínimo de edad
mean(titanic$Age, na.rm=T)

summary(titanic$Age, na.rm=T)

## Ejercicio, selecciona las filas de menores de edad y
# guardalo en un nuevo dataframe llamado menores

menores <- titanic[titanic$Age < 18,]

## Ejercico mejorado. Vamos a quitar los NA que aparecen en menores
menores <- titanic[!is.na(titanic$Age) & titanic$Age < 18,]
View(menores)

# Filtra aquellas mujeres de primera clase y extrae
# las columnas Fare y Survived

titanic[titanic$Sex =='female'& titanic$Pclass ==1,c("Fare","Survived")]

## Porcentaje de supervivencia en este grupo.
mean(MujeresDePrimera$Survived)
#or
sum(MujeresDePrimera$Survived)/nrow(MujeresDePrimera)
#or
aggregate(cbind(Survived)~(Sex +Pclass),titanic,mean)

#EJERCICIOS PARA CASA
## 1.Media de edad de hombres que sobrevivieron

mean(titanic[titanic$Sex=='male' & titanic$Survived==1,"Age"],na.rm=T)
#or
aggregate(Age~Sex+Survived, titanic, mean)

## 2.Cuantas personas sobrevivieron
sum(titanic$Survived==1)
table(titanic$Survived)


## 3.Cuantas personas fallecieron
sum(titanic$Survived==0)
table(titanic$Survived)

## 4.Cuantas personas embarcaron en el Titanic
sum(!titanic$Embarked=="")
table(titanic$Embarked)

## 5.Ratio Entre personas de primera clase y tercera

table(titanic$Pclass)
sum(titanic$Pclass==1)/sum(titanic$Pclass==3) #por cada mujer de primera hay 0.43 de tercera


## 6.Seleccionar columna Age y Sex para personas de primera clase
titanic[titanic$Pclass==1,c("Age","Sex")]


## 7.Calcula la mÃ¡scara para seleccionar los supervivientes
## de tercera clase o los hombres de primera que fallecieron

titanic[titanic$Survived==1 & titanic$Pclass==3 | titanic$Survived==0 & titanic$Pclass==1,]

## 8.Correlacion entre edad y fare para cada sexo

cor(titanic$Age, titanic$Fare, "complete")

## 9. Crea una nueva columna en "titanic" que se llame riesgo que valga
# para cada grupo el siguiente valor:
#            Mujer    Hombre
# 1a clase   1        2
# 2a clase   2        3
# 3a clase   3        4

#SOLUCION: En primer lugar crearemos un vector de caracter numérico y longitud la del
#data frame titanic al que denominamos "Riesgo"
Riesgo<- vector(mode="numeric",length = 891)

#A continuación la incorporamos en titanic
titanic=data.frame(titanic,Riesgo)
View(titanic)

#Por último crearemos asignaremos los valores para cada máscara

#Mujer primera clase valor 1
titanic[titanic$Sex =="female" & titanic$Pclass==1,"Riesgo"] <-1
#Mujer segunda clase valor 2
titanic[titanic$Sex =="female" & titanic$Pclass==2,"Riesgo"] <-2
#Mujer tercera clase valor 3
titanic[titanic$Sex =="female" & titanic$Pclass==3,"Riesgo"] <-3
#Hombre primera clase valor 2
titanic[titanic$Sex =="male" & titanic$Pclass==1,"Riesgo"] <-2
#Hombre segunda clase valor 3
titanic[titanic$Sex =="male" & titanic$Pclass==2,"Riesgo"] <-3
#Hombre tercera clase valor 4
titanic[titanic$Sex =="male" & titanic$Pclass==3,"Riesgo"] <-4


## 10. Crea otra columna desviacionFare con la diferencia entre Fare y la media
# de todos los "Fare" del dataset.

#Solución: en primer lugar creamos el vector "DesviaciónFare" y a continuación 
#la incorporamos al DF "titanic"
DesviacionFare <- vector(mode = "numeric", length = 891)
titanic=data.frame(titanic,DesviacionFare)

mean(titanic$Fare) #A continuación calculamos la media de todos los fare 

titanic$DesviacionFare <-(titanic$Fare - mean(titanic$Fare)) #Por último 
#completamos los datos de la columna "DesviacionFare" con la desviación

# Calcula el mÃ?nimo y mÃ¡ximo de esta nueva variable para cada combinaciÃ³n
# de sexo y clase.

aggregate(DesviacionFare~Sex+Pclass,titanic,max)
aggregate(DesviacionFare~Sex+Pclass,titanic,min)

## 11. Mira la ayuda de xtabs y presenta los mÃ?nimos de otra manera con
# esta funciÃ³n 
(WIP)


#útil http://www.dma.ulpgc.es/profesores/personal/stat/cursoR4ULPGC/index.html
