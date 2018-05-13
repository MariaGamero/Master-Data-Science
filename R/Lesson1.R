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
