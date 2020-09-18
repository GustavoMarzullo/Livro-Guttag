import numpy as np
import sys
sys.setrecursionlimit(1500000000)
import pylab as py
#fazendo o log natural por integral
def f(x):
    return (1)/(x+1)
def simp(b,n=10 ):
    if b==0:
        return 0
    deltax=(b)/n
    
    soma_I= f(0)+f(b)

    soma_II=0 
    for i in np.arange(deltax,b,2*deltax):
        y=f(i)
        soma_II+=y

    soma_III=0 
    for i in np.arange(2*deltax,b,2*deltax):
        y=f(i)
        soma_III+=y

    integral=(soma_I+4*soma_II+2*soma_III)*(deltax/3)
    return integral

def ln_int(b):
    assert b>0,('Fora do domínio.')
    return simp(b-1)

#fazendo o log natual por Taylor
def ln_taylor(b,n_int=50):
    soma=0
    b=b-1
    L=[]
    float(b)
    for n in range(1,n_int+1):
        y=((-1)**(n+1))*((b**n)/n)
        soma+=y
        L.append(soma)
    py.figure(1)
    py.plot(L)
    py.show()
    print(soma)
        
