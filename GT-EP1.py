# Ep1 - Numerico  Gabriel Hirata e Thiago Takabatake
import numpy as np     
import math         

#########################################################################################
# primeira Tarefa

def sincos(a,b):      # funcao que calcula os valores de sin(s) e cos(c)
                      # a serem utilizados na Rotacao de Givens
    if abs(a)>abs(b):    # se |W[i][k]| > |W[j][k]|
        tau = -b/a       
        c = 1/math.sqrt(1+tau**2)
        s = c*tau
    else:                # caso contrario
        tau = -a/b
        s = 1/math.sqrt(1+tau**2)
        c = s*tau
    return c,s

def rotgivens(X,n,m,i,j,k,c,s):
    # aplica a Rotacao de Givens nas linhas i e j da matriz X
    for r in range(k,m):
        aux = c*X[i][r] - s*X[j][r]
        X[j][r] = s*X[i][r] + c*X[j][r]
        X[i][r] = aux

def somatorio(W,x,k):
    soma = 0
    for j in range(k+1,m):
        soma = soma + W[k][j]*x[j]
    return soma

def fatqr(W,b,n,m):
    for k in range(m):
        for j in range(n-1,k,-1):
            i = j-1
            if W[j][k] != 0:
                e = W[i][k]
                f = W[j][k]
                c,s = sincos(e,f)
                rotgivens(W,n,m,i,j,k,c,s)
                rotgivens(b,n,1,i,j,0,c,s)
    for k in range(m-1,-1,-1):
        x[k] = (b[k]- somatorio(W,x,k))/W[k][k]

def criamatriz(n,m,item):    # função para criar as matrizes dos testes a) e b) 
                             # dados no enunciado
    if item == "a":
        W = np.zeros((n,m))    # cria matriz de zeros
        b = np.ones((n,1))     # cria matriz de "uns"
        # laco para preencher a matriz conforme pedido no enunciado
        # como indices de matrizes começam em 0 em python, faz-se -1 nos indices de W
        for i in range(1,n+1):  
            for j in range(1,m+1):                
                if abs(i-j)==1:
                    W[i-1][j-1]=1
                else:
                    W[i-1][j-1]=0
                W[i-1][i-1]=2
    if item == "b":
        W = np.zeros((n,m))      # cria matriz de zeros
        b = np.zeros((n,1))      # cria matriz de zeros
        # laco para preencher a matriz W conforme pedido no enunciado
        for i in range(1,n+1):
            for j in range(1,m+1):
                if abs((i-1)-(j-1)) <= 4:
                    W[i-1][j-1] = 1/(i+j-1)
                else:
                    W[i-1][j-1] = 0
        # laco para preencher a matriz b conforme pedido no enunciado
        for i in range(1,n+1):
            b[i-1] = i
    return W,b

# realiza testes a) ou b)
item = input("Qual o item ('a' ou 'b') a ser testado: ")  
if item == "a":
    n = 64
    m = 64
    W,b = criamatriz(n,m,item)
    x = np.zeros((m,1))
elif item == "b":
    n = 20
    m = 17
    W,b = criamatriz(n,m,item)
    x = np.zeros((m,1))
else:
    print("Teste nao existente.")

fatqr(W,b,n,m)
print(x)

def somatorio2(W,H,k,j):
    soma = 0
    for i in range(k+1,p):
        soma = soma + W[k][i]*H[i][j]
    return soma

def variossistemas(n,p,m,W,A,H):
    for k in range(p):
        for j in range(n-1,k,-1):
            i = j-1
            if W[j][k] != 0:
                e = W[i][k]
                f = W[j][k]
                c,s = sincos(e,f)
                rotgivens(W,n,p,i,j,k,c,s)
                rotgivens(A,n,m,i,j,0,c,s)
    for k in range(p-1,-1,-1):
        for j in range(m):
            H[k][j] = (A[k][j]- somatorio2(W,H,k,j))/W[k][k]

def criamatriz2(n,p,m,item):    # função para criar as matrizes dos testes a) e b) 
                                # dados no enunciado
    if item == "c":
        W = np.zeros((n,p))    # cria matriz de zeros
        A = np.ones((n,m))     # cria matriz de "uns"
        # laco para preencher a matriz conforme pedido no enunciado
        # como indices de matrizes começam em 0 em python, faz-se -1 nos indices de W
        for i in range(1,n+1):  
            for j in range(1,p+1):                
                if abs(i-j)==1:
                    W[i-1][j-1]=1
                else:
                    W[i-1][j-1]=0
                W[i-1][i-1]=2
        for i in range(1,n+1):        
            A[i-1][1] = i
            A[i-1][2] = 2*i-1
    if item == "d":
        W = np.zeros((n,p))      # cria matriz de zeros
        A = np.ones((n,m))       # cria matriz de "uns"
        # laco para preencher a matriz W conforme pedido no enunciado
        for i in range(1,n+1):
            for j in range(1,p+1):
                if abs((i-1)-(j-1)) <= 4:
                    W[i-1][j-1] = 1/(i+j-1)
                else:
                    W[i-1][j-1] = 0
        # laco para preencher a matriz b conforme pedido no enunciado
        for i in range(1,n+1):        
            A[i-1][1] = i
            A[i-1][2] = 2*i-1
    return W,A

# realiza testes c) ou d)
item = input("Qual o item ('c' ou 'd') a ser testado: ")  
if item == "c":
    n = 64
    p = 64
    m = 3
    W,A = criamatriz2(n,p,m,item)
    H = np.zeros((p,m))
elif item == "d":
    n = 20
    p = 17
    m = 3
    W,A = criamatriz2(n,p,m,item)
    H = np.zeros((p,m))
else:
    print("Teste nao existente.")

variossistemas(n,p,m,W,A,H)
print(H)

#########################################################################################
# Segunda Tarefa
