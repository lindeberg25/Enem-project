'''
Created on 10  de abril de 2019

@author: lindeberg
'''
#Esta funcao - LerCluster - recebe como entrada a matrix de dissimilaridade de cada cluster e 
# organiza, em ordem decrescente de distancia, os cadidatos aos seus respectivos  medoids dentro de cada cluster. Adicionalmente, as informacoes 
# complementares dos candidatos sao acrescidas 

import csv
import pandas as pd
from Candidato import Candidato
from prettytable import PrettyTable


medoid=164
listaDeCandidatos=[]

x = PrettyTable()


with open('C:/Users/Lindeberg/Documents/doutorado/Enem 2017/DADOS/disMatrix-c06M.csv') as csv_matrix:
    csv_reader_matrix = csv.reader(csv_matrix)
    rows = list(csv_reader_matrix)
    
    row=rows[medoid]
    
    # Elimina o primeiro elemento da linha 
    del row[0]
   
    count=1

    # criar candidatos com a posicao e distancia ao medoid 
    for distancia in row: 
          
        candidato = Candidato(count, distancia)
        count = count + 1
        listaDeCandidatos.append(candidato)
    
    csv_matrix.close()    
    #Abre o arquivo cluster para completar os candidatos com os outros atributos
    #encoding='iso-8859-1'
    df = pd.read_csv('C:/Users/Lindeberg/Documents/doutorado/Enem 2017/DADOS/c06M.csv', encoding='iso-8859-1')
    lista = ['NU_INSCRICAO', 'NO_MUNICIPIO_RESIDENCIA', 'SG_UF_RESIDENCIA', 'NU_IDADE', 'TP_SEXO', 'TP_ESCOLA','TP_ENSINO','NO_MUNICIPIO_PROVA','SG_UF_PROVA','CO_PROVA_CN','CO_PROVA_CH','CO_PROVA_LC','CO_PROVA_MT','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_COMP1','NU_NOTA_COMP2','NU_NOTA_COMP3','NU_NOTA_COMP4','NU_NOTA_COMP5','NU_NOTA_REDACAO','Q006']
   
    new_df = df[lista]
    
    #passa por todos os candidatos adicionando informacoes importante de cada elemento no cluster

    for itemCandidato in listaDeCandidatos:
       
        NU_INSCRICAO = new_df.iloc[itemCandidato.posicao -1,0]   
        NO_MUNICIPIO_RESIDENCIA = new_df.iloc[itemCandidato.posicao -1,1]
        SG_UF_RESIDENCIA = new_df.iloc[itemCandidato.posicao -1,2]
        NU_IDADE = new_df.iloc[itemCandidato.posicao -1,3] 
        TP_SEXO = new_df.iloc[itemCandidato.posicao -1,4]
        TP_ESCOLA = new_df.iloc[itemCandidato.posicao -1,5]
        TP_ENSINO = new_df.iloc[itemCandidato.posicao -1,6]
        NO_MUNICIPIO_PROVA = new_df.iloc[itemCandidato.posicao - 1 ,7]
        SG_UF_PROVA = new_df.iloc[itemCandidato.posicao -1,8]
        CO_PROVA_CN = new_df.iloc[itemCandidato.posicao -1,9]
        CO_PROVA_CH = new_df.iloc[itemCandidato.posicao -1,10]
        CO_PROVA_LC = new_df.iloc[itemCandidato.posicao -1,11]
        CO_PROVA_MT = new_df.iloc[itemCandidato.posicao -1,12]
        NU_NOTA_CN = new_df.iloc[itemCandidato.posicao -1,13]
        NU_NOTA_CH = new_df.iloc[itemCandidato.posicao -1,14]
        NU_NOTA_LC = new_df.iloc[itemCandidato.posicao -1,15]
        NU_NOTA_MT = new_df.iloc[itemCandidato.posicao -1,16]
        NU_NOTA_COMP1 = new_df.iloc[itemCandidato.posicao -1,17]
        NU_NOTA_COMP2 = new_df.iloc[itemCandidato.posicao -1,18]
        NU_NOTA_COMP3 = new_df.iloc[itemCandidato.posicao -1,19]
        NU_NOTA_COMP4 = new_df.iloc[itemCandidato.posicao -1,20]
        NU_NOTA_COMP5 = new_df.iloc[itemCandidato.posicao -1,21]
        NU_NOTA_REDACAO = new_df.iloc[itemCandidato.posicao -1,22]
        Q006 = new_df.iloc[itemCandidato.posicao -1,23]
         
         
         
        itemCandidato.completaCadidato(NU_INSCRICAO, NO_MUNICIPIO_RESIDENCIA, SG_UF_RESIDENCIA, NU_IDADE, TP_SEXO, TP_ESCOLA, TP_ENSINO,NO_MUNICIPIO_PROVA,SG_UF_PROVA,CO_PROVA_CN,CO_PROVA_CH,CO_PROVA_LC,CO_PROVA_MT, NU_NOTA_CN, NU_NOTA_CH, NU_NOTA_LC, NU_NOTA_MT, NU_NOTA_COMP1, NU_NOTA_COMP2, NU_NOTA_COMP3, NU_NOTA_COMP4,NU_NOTA_COMP5,NU_NOTA_REDACAO,Q006)
    
    listaDeCandidatos.sort(key=lambda x: x.distancia)
    
    # contador criado para setar o numero de candidatos proximos apresentado por cluster (neste caso apenas 6 candidatos)
    count = 1
    
    x.field_names = ["Inscricao", "Distancia", "    Residencia   ", "Res UF", "   Municipio de Prova   ", "Mun UF", "CN", "CH", "LC", "MT"]
    for item in listaDeCandidatos:
        
        if count < 7:
            x.add_row([item.NU_INSCRICAO, format(float(item.distancia),'.2f'), item.NO_MUNICIPIO_RESIDENCIA, item.SG_UF_RESIDENCIA, item.NO_MUNICIPIO_PROVA,item.SG_UF_PROVA,item.CO_PROVA_CN,item.CO_PROVA_CH,item.CO_PROVA_LC,item.CO_PROVA_MT])           
        count = count +1  
 
    #print x
    table_txt = x.get_string().encode("iso-8859-1")
    print table_txt
    with open('output-c03.txt','w') as file:
        file.write(table_txt)
   
    