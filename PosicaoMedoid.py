'''
Created on 01 de abril de 2019

@author: lindeberg
'''
# Esta funcao localiza a posicao do medoid no csv


import pandas as pd

# Abre o arquivo cluster 
df = pd.read_csv("C:/Users/Lindeberg/Documents/doutorado/Enem 2017/DADOS/c06M.csv")

df_nu_inscricao = df['NU_INSCRICAO']


df_medoid = pd.read_csv("C:/Users/Lindeberg/Documents/doutorado/Enem 2017/DADOS/medoids.csv")
df_medoids = df_medoid['MEDOIDS']

PosicoesMedoids=[]
count = 1    
for row in df_nu_inscricao:
     
    for medoid in df_medoids:
        if row == medoid:
            PosicoesMedoids.append(count) 
                
    count = count + 1
for posicao in PosicoesMedoids:
    print (posicao)
    