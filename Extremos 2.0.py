#achar o máximo ou mínimo de uma função
import numpy as np

def maximo(f,a,b,deltax=0.001):
    '''Retorna o máximo da função f no intervalo [a,b] e o seu respectivo valor no domínio(x,y). Se houver dois valores máximos iguais retorna o mais a direita.'''
    valor=[]
    valor.append(a)
    valor.append(f(a))  
    for i in np.arange(a+deltax,b+deltax,deltax):
        if f(i)<valor[1]:
            continue
        else:
            valor[0]=i
            valor[1]=f(i)
    return valor[0],valor[1]

def minimo(f,a,b,deltax=0.001):
    '''Retorna o máximo da função f no intervalo [a,b] e o seu respectivo valor no domínio(x,y). Se houver dois valores minimos iguais retorna o mais a direita.'''
    valor=[]
    valor.append(a)
    valor.append(f(a))  
    for i in np.arange(a+deltax,b+deltax,deltax):
        if f(i)>valor[1]:
            continue
        else:
            valor[0]=i
            valor[1]=f(i)
    return valor[0],valor[1]