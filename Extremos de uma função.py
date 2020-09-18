#achar o máximo de uma função
import numpy as np
def maxfun(a,b,deltax=1e-3):
    assert b>a,('Erro de matemática: b tem que ser maior que a.')
    maximo_y=f(a)
    maximo_x=a
    for i in np.arange(a,b+deltax,deltax):
        if f(i)>maximo_y:
            maximo_y=f(i)
            maximo_x=i
    iteracoes=(b+deltax-a)/deltax +1
    print('y=',str(maximo_y))
    print('x=',str(maximo_x))
    print('Iterações:',str(round(iteracoes)))

#achar o máximo de uma função
def minfun(a,b,deltax=1e-3):
    assert b>a,('Erro de matemática: b tem que ser maior que a.')
    minimo_y=f(a)
    minimo_x=a
    for i in np.arange(a,b+deltax,deltax):
        if f(i)<minimo_y:
            minimo_y=f(i)
            minimo_x=i
    iteracoes=(b+deltax-a)/deltax +1
    print('y=',str(minimo_y))
    print('x=',str(minimo_x))
    print('Iterações:',str(round(iteracoes)))
