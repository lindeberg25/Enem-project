library(dplyr) # for data cleaning
library(cluster) # for gower similarity and pam
library(ggplot2)
library(mclust)
require(dplyr)
library(ClusterR)
library(cluster)


set.seed(123)

dados <- read.csv("/home/lindeberg/Enem 2017/DADOS/clusterCompleto-splited-Number2-35.csv")

dim(dados)
# selecao das colunas que servem  de entrada para o calculo da distancia de Hamming e para o metodo pam
dados_colum_selec = dados[, 25:199]

###############################
### Calculo da matriz de dissimilaridade utilizando programação paralela (7 cores)
### Compara-se o tempo de execução paralela (5 cores) com o tempo de processamento não paralelo (1 core)
#Estimativa do tempo gasto para calcular a matriz de dissmilaridade
system.time(
  # Calculo da matriz de dissmilaridade usando distencia de Hamming em paralelo
  { hamming_dist = distance_matrix(dados_colum_selec, method = "hamming",  upper = TRUE, diagonal = TRUE, threads = 7)})



# Aplicacao do metodo pam para 6 clusters e o conjunto inicial de meddoids
pm <- pam(hamming_dist, 6,  medoids = c(951, 1321, 1653, 2081, 2943, 4270), diss=TRUE, do.swap = FALSE)



# os 6 clusters são separados 
c01 <- dados[which(pm$clustering == 1),]
c02 <- dados[which(pm$clustering == 2),]
c03 <- dados[which(pm$clustering == 3),]
c04 <- dados[which(pm$clustering == 4),]
c05 <- dados[which(pm$clustering == 5),]
c06 <- dados[which(pm$clustering == 6),]


# os clusters são salvos para analise por um script em python. O script possui a função de selecionar os candidatos mais próximos 
# do medoid
write.csv(c01, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/c01.csv")
write.csv(c02, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/c02.csv")
write.csv(c03, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/c03.csv")
write.csv(c04, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/c04.csv")
write.csv(c05, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/c05.csv")
write.csv(c06, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/c06.csv")


# Como o metodo daisy não possui distância de Hamming, utlizamos distência de gower, que possui o mesmo 
# comportamente de Hamming para dados qualitativos. Abaixo são calculadas as matrizes de dissimilaridade para cada cluster
# Essa matrizes de dissmilaridade são fornecidas como entrada  para um script em python que seleciona os candidatos mais próximos 
# do medoid

c01_colum_selec = c01[, 25:199]
matrixDissimilaridadeC01 <- daisy(c01_colum_selec, metric = "gower", stand = FALSE)
disMatrix01 = as.matrix(matrixDissimilaridadeC01) # via as.matrix.dist(.)
write.csv(disMatrix01, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/disMatrix-c01.csv")

c02_colum_selec = c02[, 25:199]
matrixDissimilaridadeC02 <- daisy(c02_colum_selec, metric = "gower", stand = FALSE)
disMatrix02 = as.matrix(matrixDissimilaridadeC02) # via as.matrix.dist(.)
write.csv(disMatrix02, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/disMatrix-c02.csv")

c03_colum_selec = c03[, 25:199]
matrixDissimilaridadec03 <- daisy(c03_colum_selec, metric = "gower", stand = FALSE)
disMatrix03 = as.matrix(matrixDissimilaridadec03) # via as.matrix.dist(.)
write.csv(disMatrix03, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/disMatrix-c03.csv")

c04_colum_selec = c04[, 25:199]
matrixDissimilaridadec04 <- daisy(c04_colum_selec, metric = "gower", stand = FALSE)
disMatrix04 = as.matrix(matrixDissimilaridadec04) # via as.matrix.dist(.)
write.csv(disMatrix04, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/disMatrix-c04.csv")

c05_colum_selec = c05[, 25:199]
matrixDissimilaridadec05 <- daisy(c05_colum_selec, metric = "gower", stand = FALSE)
disMatrix05 = as.matrix(matrixDissimilaridadec05) # via as.matrix.dist(.)
write.csv(disMatrix05, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/disMatrix-c05.csv")

c06_colum_selec = c06[, 25:199]
matrixDissimilaridadec06 <- daisy(c06_colum_selec, metric = "gower", stand = FALSE)
disMatrix06 = as.matrix(matrixDissimilaridadec06) # via as.matrix.dist(.)
write.csv(disMatrix06, file = "/home/lindeberg/doutorado/Enem 2017/DADOS/disMatrix-c06.csv")


