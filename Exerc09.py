#ATIVIDADE PEDIDA: (Prof.Ronaldo)####################################################################################################################################################
#CT0109 – Nona contribuição da primeira etapa                                                                                                                                       #
#Implementar o Radix sort e imprimir os graficos conforme segue:                                                                                                                    #
#                                                                                                                                                                                   #
#   *Tamanho da lista de números x Tempo para ordenar pelo método - OBRIGATÓRIO!                                                                                                    #
#   [Tamanho da lista x Quantidade de operações (Número de comparações)] X <- Não foi feito pois não encontrou-se nenhuma "iteração(condicional)" ou "SWAP" para o algoritmo pedido!#
#                                                                                                                                                                                   #
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 100K, 200K, 400K, 500K, 1M, 2M.                                                                          #
#####################################################################################################################################################################################

#"Importação das devidas bibliotecas ;)"

import sys

import math

import random
from random import randint

import timeit

import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt

###############################################################################{
#"Declarações iniciais..."
mpl.use('Agg')
mpl.rc('lines', linewidth=1.5)
plt.style.use('fast')
sys.setrecursionlimit(10**9)
###############################################################################}         

#"Segunda Função responsável pela criação do gráfico(x,y) para estudo do desempenho de algoritmo" *(Usada para criar o gráfico dos 3 casos apresentados juntos na mesma malha)
#Implementação do professor + implementação do aluno####################################################################################################{      
def desenhaGrafico2(x, y, yde, yce, file_name, label, label2, label3, file_title, line_color, line_color2, line_color3, xl, yl):                                                                                               #
    fig = plt.figure(figsize=(20, 20))                                                                                                                                                                 
    ax = fig.add_subplot(111)                                                                                                                          
    ax.plot(x,y, color=line_color,linestyle = '-',linewidth=5,label = label)                           
    ax.plot(x,yde, color=line_color2,linestyle = '-',linewidth=3,label = label2)                     
    ax.plot(x,yce, color=line_color3,linestyle = '-',linewidth=1,label = label3)
                                                                     
    stemlines = plt.stem(x,y, markerfmt=' ',linefmt='k:', basefmt=' ',use_line_collection=True)                                                                                                 
    plt.setp(stemlines, 'linewidth', 1)                                                                                                                
    stemlines = plt.stem(x,yde, markerfmt=' ',linefmt='k:', basefmt=' ',use_line_collection=True)                                                                                            
    plt.setp(stemlines, 'linewidth', 1)                                                                                                                
    stemlines = plt.stem(x,yce, markerfmt=' ',linefmt='k:', basefmt=' ',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 1)
                                                                                                                                                                                                                                                                                            
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                              
    plt.ylabel(yl)                                                                                                                                                                                                                         
    plt.xlabel(xl)                                                                                                                                                                                                                         
    plt.title(file_title)                                                                                                                                                                                                            
    fig.savefig(file_name)                                                                                                                                                                                                          
########################################################################################################################################################}       

#"Função De Ordenação Auxiliar do Radix Sort: Counting Sort"
#Implementação do aluno#########################################################################{
def countingSort(lista, exp1):                                                                                                                                                                                                                            
    n = len(lista) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (lista[i]//exp1) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (lista[i]//exp1) 
        output[ count[ (index)%10 ] - 1] = lista[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(lista)): 
        lista[i] = output[i] 
################################################################################################}

#"Função Radix Sort(+Counting Sort)"
#Implementação do aluno#########################################################################{
def radixSort(lista):                                                                                                                                                                                                                            
    # Find the maximum number to know number of digits 
    max1 = max(lista) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1//exp > 0: 
        countingSort(lista,exp) 
        exp *= 10
################################################################################################}

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente ou em certa ordem específica(Para essa NONA ATIVIDADE será em ordem ALEATÓRIA) e retorna os devidos gráficos comparativos"
#Obs.:(O que estiver comentado no código da função abaixo foi usado para gerar os outros gráficos)
#Implementação do aluno##########################################################################################################################################################################################################################################################################################################################################{
def cria_Graficos(lista_entrada):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #

  tempos_orden_Random = list()
  tempos_orden_Decresc = list()   
  tempos_orden_Cresc = list()
                                                                                                                                                                                                                                                                                                           
  for i in lista_entrada:                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                           
    #1) Lista Aleatória <- OBRIGATÓRIO(PEDIDO NA ATIVIDADE)                                                                                                                                                                                                                                                
    lista = list(range(0, i + 1))                                                                                                                                                                                                                                                                          
    random.shuffle(lista)
    tempos_orden_Random.append(timeit.timeit("radixSort({})".format(lista),setup="from __main__ import radixSort",number=1))

    #2) Lista já ORDENADA em ordem DECRESCENTE<- OPCIONAL(AMOSTRAGEM DO ALUNO)                                                                                                                                                                                                                              
    lista = list(range(i,-1,-1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    tempos_orden_Decresc.append(timeit.timeit("radixSort({})".format(lista),setup="from __main__ import radixSort",number=1))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #                                                                                                                                                                                                                                                                                                            #
    #3) Lista já ORDENADA em ordem CRESCENTE<- OPCIONAL(AMOSTRAGEM DO ALUNO)                                                                                                                                                                                                                               
    lista = list(range(0,i+1,1))
    tempos_orden_Cresc.append(timeit.timeit("radixSort({})".format(lista),setup="from __main__ import radixSort",number=1))                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                  
  desenhaGrafico2(lista_entrada,tempos_orden_Random,tempos_orden_Decresc,tempos_orden_Cresc,"GraficoRadixSort(Tamanho_Lista-X-Tempo_Ordenacoes).png", "Tempo(Lista->Aleatória[Counting+Radix Sort])","Tempo(Lista->Decrescente[Counting+Radix Sort])","Tempo(Lista->Crescente[Counting+Radix Sort])",'(Radix + Counting Sort - Listas: Aleatória/Decrescente/Crescente)Tamanho_Lista X Tempo_Ordenacoes','yellow','cyan','lime',"<Entradas/>","<Tempo-Saída/>")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #                                                                                                                                                                                                                                                                                                           
#################################################################################################################################################################################################################################################################################################################################################################}

#Inicialização da aplicação:
##########################################################################
lista_teste = [100000,200000,400000,500000,1000000,2000000]              #
cria_Graficos(lista_teste)                                               #
##########################################################################
#############################
################                                                       
