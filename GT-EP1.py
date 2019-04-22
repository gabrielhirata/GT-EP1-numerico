# EP1 - Numérico
import numpy as np     
import math         

# Primeira Tarefa

def sincos(a,b):      # função que calcula os valores de sin e cos a serem utilizados
                      # na Rotação de Givens
    if abs(a)>abs(b):    # se |W[i][k]| > |W[j][k]|
        tau = -b/a       
        c = 1/math.sqrt(1+tau**2)
        s = c*tau
    else:                # caso contrário
        tau = -a/b
        s = 1/math.sqrt(1+tau**2)
        c = s*tau
    return c,s

def rotgivens(W,n,m,i,j,c,s):
    for r in range(1,n):
        aux = c*W[i][r]-s*W[j][r]
        W[j][r] = s*W[i][r]+c*W[j][r]
        W[i][r] = aux
    return W

def fatqr(W,n,m,i,j,c,s):
    for k in range(1,m):
        for j in range(n,k+1,-1):
            i=j-1
            if W[j][k] != 0:
                rotgivens(W,n,m,i,j,c,s)
#    for k in range(m,1,-1):
#        x[k]=(b[k]-

def criamatriz(n,m,item):    # função para criar as matrizes dos testes a) e b) 
                             # dados no enunciado
    if item == "a":
        W = np.zeros((n,m))  # cria matriz de zeros
        b = np.ones((n,1))     # cria matriz de "uns"
        # laço para preencher a matriz conforme pedido no enunciado
        # como índices de matrizes começam em 0 em Python, faz-se -1 nos índices de W
        for i in range (1,n+1):  
            for j in range(1,m+1):
                W[i-1][i-1]=2
                if abs(i-j)==1:
                    W[i-1][j-1]=1
                else:
                    W[i-1][j-1]=0
    if item == "b":
        W = np.zeros((n,m))      # cria matriz de zeros
        b = np.zeros((n,1))      # cria matriz de zeros
        # laço para preencher a matriz W conforme pedido no enunciado
        for i in range (1,n+1):
            for j in range(1,m+1):
                if abs((i-1)-(j-1))<=4:
                    W[i-1][j-1]=1/(i+j-1)
                else:
                    W[i-1][j-1]=0
        # laço para preencher a matriz b conforme pedido no enunciado
        for i in range(1,n+1):
            b[i-1]=i
    return W,b

# realiza testes a) ou b)
item = input("Qual o item ('a' ou 'b') a ser testado: ")  
if item == "a":
    a,b = criamatriz(64,64,item)
elif item == "b":
    a,b = criamatriz(20,17,item)
else:
    print("Teste não existente.")
    
# c,s = sincos(2,-1)
# print(c)
# print(s)