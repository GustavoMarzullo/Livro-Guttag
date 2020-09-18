import random
import matplotlib.pyplot as plt
import scipy.stats as stats

def direcao():
    '''Retorna 4 direções aleatórias.'''
    return random.choice(['N','S','L','O'])

def caminhada(n,xmax,ymax):
    '''Dá n passo aleatórios'''
    x,y=0,0
    for i in range(n):
        a=direcao()
        if a=='N':
            y+=1
            if y>= ymax:
                y=ymax
        elif a=='S':
            y-=1
            if abs(y)>= ymax:
                y=-ymax
        elif a=='O':
            x-=1
            if abs(x)>= xmax:
                x=-xmax
        else:
            x+=1
            if x>= xmax:
                x=xmax
    return x,y

def dist(n,xmax,ymax):
    '''Calcula a distância do ponto (x,y) até o ponto (0,0).'''
    ponto=caminhada(n,xmax,ymax)
    xa=ponto[0]
    ya=ponto[1]
    return (xa**2 + ya**2)**0.5

def dist_media(n,x,xmax,ymax):
    '''Retorna a distância média para x séries de caminhadas.'''
    distancias=[]
    for i in range(x):
        distancias.append(dist(n,xmax,ymax))
    return stats.tmean(distancias)
     
def grafico():
    medias=[]
    n=[]
    i=200
    while i<3100:
        medias.append(dist_media(i,1000,50,50))
        n.append(i)
        i+=100
    plt.figure(1)
    plt.plot(n,medias,color='grey', linestyle='dashed', marker='o',markerfacecolor='black', markersize=4)
    plt.title('Bêbado')
    plt.xlabel('n')
    plt.ylabel('Distância')
    plt.show()

def destino(n,xa,ya,xmax,ymax,series=1000):
    '''Retorna a média da probabilidade de tantas séries do bêbado chegar no ponto (xa,ya) com n passos.
OBS: sempre será minúscula.'''
    x,y=0,0
    sucessos=0
    for i in range(series):
        for i in range(n):
            a=direcao()
            if a=='N':
                y+=1
                if y>= ymax:
                    y=ymax
                if x==xa and y==ya:
                    sucessos+=1
                    break
            elif a=='S':
                y-=1
                if abs(y)>= ymax:
                    y=-ymax
                if x==xa and y==ya:
                    sucessos+=1
                    break
            elif a=='O':
                x-=1
                if abs(x)>= xmax:
                    x=-xmax
                if x==xa and y==ya:
                    sucessos+=1
                    break
            else:
                x+=1
                if x>= xmax:
                    x=xmax
                if x==xa and y==ya:
                    sucessos+=1
                    break
    return (sucessos/series)

def passos(xa,ya,xmax,ymax,series=1000):
    '''Retorna a média de tantas séries de quantos passos o bêbado leva pra chegar em tal ponto.'''
    lista_passos=[]
    for i in range(series):
        x,y=0,0
        passos=1
        while x!=xa and y!=ya:
            a=direcao()
            if a=='N':
                passos+=1
                y+=1
                if y>= ymax:
                    y=ymax
            elif a=='S':
                passos+=1
                y-=1
                if abs(y)>= ymax:
                    y=-ymax
            elif a=='O':
                passos+=1
                x-=1
                if abs(x)>= xmax:
                    x=-xmax
            else:
                passos+=1
                x+=1
                if x>= xmax:
                    x=xmax
        lista_passos.append(passos)
    print('Média='+str(round(stats.tmean(lista_passos),5))+'\nDesvio-padrão='+str(round(stats.tstd(lista_passos),5)))

