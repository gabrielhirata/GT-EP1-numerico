# EP1 - Numérico
import numpy as np     
import math         

# Primeira Tarefa

def sincos(a,b):
    if abs(a)>abs(b):
        tau = -b/a
        c = 1/math.sqrt(1+tau**2)
        s = c*tau
    else:
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

def criamatriz(n,m,item):
    if item == "a":
        W = np.zeros((n-1,m-1))
        b = np.ones((n-1,1))
        for i in range (0,n-1):
            for j in range(0,m-1):
                W[i][i]=2
                if abs(i-j)==1:
                    W[i][j]=1
                else:
                    W[i][j]=0
    if item == "b":
        W = np.zeros((n,m))
        b = np.zeros((n,1))
        for i in range (1,n+1):
            for j in range(1,m+1):
                if abs((i-1)-(j-1))<=4:
                    W[i-1][j-1]=1/(i+j-1)
                else:
                    W[i-1][j-1]=0
        for i in range(1,n+1):
            b[i-1]=i
    return W,b

a,b = criamatriz(64,64,"a")
print(a)
print(b)
# c,s = sincos(2,-1)
# print(c)
# print(s)