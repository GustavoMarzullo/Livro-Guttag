#Achar o valor máximo da função em dado intervalo
import numpy
def f(x):
    y=(x**2) + 2*x + 5
    return y
def valmax(a,b,erro=0.001):
    L=[]
    for i in numpy.arange(a,b+erro,erro):
        z=f(i)
        L.append(z)
    maximo=max(L)
    print('O valor máximo de '+str(a)+' até '+str(b)+' é '+ str(maximo))
def valmin(a,b,erro=0.001):
    L=[]
    for i in numpy.arange(a,b+erro,erro):
        z=f(i)
        L.append(z)
    maximo=min(L)
    print('O valor mínimo de '+str(a)+' até '+str(b)+' é '+ str(maximo))    
