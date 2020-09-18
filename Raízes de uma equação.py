#raízes de uma equação
#You may say ain't free. But it don't worry me.


from numpy import *
import decimal
import time

def sinal(x):
    '''Função sinal. Retorna -1 se x<0, 0 se x=0 e 1 se x>0.'''
    if x>0:
        return 1.0
    elif x<0:
        return -1.0
    else:
        return 0.0

def num_casas(n):
    '''Retorna quantas casa decimais tem um número.'''
    return -1*decimal.Decimal(str(n)).as_tuple().exponent

def raizbi(f,a,b,dx=0.002):
    '''Método da busca incremetal de raíz.\nProcura uma raíz no intervalo [a,b]. Retorna um resultado (raiz,erro).'''
    x1=a
    f1=f(x1)
    x2=a+dx
    f2=f(x2)
    while sinal(f1)==sinal(f2):
        if x1>=b:
                return str('Sem raíz no intervalo '+'['+str(a)+','+str(b)+']')
        x1=x2
        f1=f(x1)
        x2=x1+dx
        f2=f(x2)
        media=(x1+x2)/2
    return round(media,num_casas(dx/2)),dx/2

def raizbs(f,a,b,epsilon=0.001):
    '''Método da bisseção para achar a raíz da função f. Faz a bisseção até que |x2-x1|<=epsilon.'''
    x1=a
    f1=f(x1)
    if f1==0.0:
        return x1
    x2=b
    f2=f(x2)
    if f2==0.0:
        return x2
    while abs(x2-x1)>=epsilon:
        x3=(x1+x2)/2
        f3=f(x3)
        if sinal(f2)!=sinal(f3):
            x1=x3
            f1=f3
        else:
            x2=x3
            f2=f3
    media=(x1+x2)/2
    return round(media,num_casas(epsilon))

def ridder(f,a,b):
    '''Método de Ridder para raíz de uma função f.'''
    for i in range(30):
        c=(a+b)/2
        d=c+(c-a)*((sinal(f(a)-f(b))*f(c))/(((f(c))**2-f(a)*f(b))**0.5))
        if sinal(f(d))==1:
            b=d
        else:
            a=d
    return d
            
        
            
