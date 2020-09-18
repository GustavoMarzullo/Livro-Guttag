import random

def devp(X):
    media=sum(X)/len(X)
    somatorio=0.0
    for i in X:
        somatorio+=(i-media)**2
    return (somatorio/len(X))**0.5



def dado():
    '''Retorna um número aleatório de 1 a 6.'''
    return random.choice([1,2,3,4,5,6])

def lance_unico(n):
    '''Retorna a probabilidade de sair 1-2 no dado. n é um múltiplo de 6.'''
    assert n%6==0,'O n precisa ser múltiplo de 6'
    L=[]
    sucessos=0
    for i in range(int(n)):
        L.append(dado())
        try:
            if L[i-1]==1 and L[i]==2:
                sucessos+=1
        except IndexError:
            continue
    return(sucessos/n)

def lance(x,n):
    '''Retorna a probabilidade de sair 1-2 no dado. x séries de n jogadas'''
    resultados=[]
    for i in range(x):
        resultados.append(lance_unico(n))
    resultado=(sum(resultados)/len(resultados))
    desvio=devp(resultados)
    print('Probabilidade=',str(resultado),'\nDesvio-padrão=',str(desvio))
    
    
