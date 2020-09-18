#integral por monte carlo
#\int_{a}^{b}=(valor_médio)*(b-a)
import random
import scipy.stats as stats
import numpy as np


def ts(alpha,gl):
    '''Retorna o valor de t-student para tal alpha e tal gis graus de liberdade.'''
    return stats.t.ppf(1-(alpha/2), gl)


def siginificativos(n):
    '''Retorna o número de algarismos siginificativos de um número.'''
    return abs(int(np.floor(np.log10(abs(n)))))


def integral(f,a,b,n=1000,x=100):
    '''Retorna a integral com x séries de n pontos de a até b de uma função f definida anteriormente. Retorna também o intervalo de confiança(IC).'''
    valores_medios=[]
    for i in range(x):
        valor=0.0
        for i in range(n): 
            valor+=f(random.uniform(a,b))
        valores_medios.append(valor/n*(b-a))
    IC=ts(0.05,x-1)*(stats.tstd(valores_medios)/(x**0.5))
    valor_medio=stats.tmean(valores_medios)
    casas=siginificativos(IC)
    return round(valor_medio,casas),round(IC,casas) 


