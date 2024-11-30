# data preprocesing

# importar el dataset
dataset = read.csv("Data.csv")

# Sepaprar el dataset en un conjunto de entrenamiento y uno de pruebas
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)