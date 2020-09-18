import random
import matplotlib.pyplot as plt
import numpy
#coração: x**2+(y-(x**2)**(1/3))**2 <= 1
#x=random.uniform(-1.2,1.2)
#y=random.uniform(-1.1,1.6)
def devp(X):
    media=sum(X)/len(X)
    somatorio=0.0
    for i in X:
        somatorio+=(i-media)**2
    return (somatorio/len(X))**0.5

def jogar(n,grafico=True):
    '''Joga aleatoriamente n vezes as agulhas do método de Monte Carlo e faz um gráfico.'''
    n=int(n)
    dentro=0
    insidex,outsidex=[],[]
    insidey,outsidey=[],[]
    for agulhas in range(1,n+1):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        if y<=2*x and y<=-2*x+2:
            dentro+=1
            insidex.append(x)
            insidey.append(y)
        else:
            outsidex.append(x)
            outsidey.append(y)
    area=dentro/n
    if grafico==True:
        fig, ax = plt.subplots(1)
        ax.scatter(insidex, insidey, c='b', alpha=0.5, edgecolor=None,marker='.')
        ax.scatter(outsidex, outsidey, c='r', alpha=0.5, edgecolor=None,marker='.')
        ax.set_aspect('equal')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Método de Monte Carlo para calcular área do <3')
        plt.annotate('Área='+str(round(area,4)),xycoords='axes fraction',xy = (1.05, 0.8))
        fig.show()
    return area

def estimativa(n,tentativas,printar=True):
    '''Joga tantas séries de agulhas n vezes.'''
    est=[]
    for i in range(tentativas):
        est.append(jogar(n,False))
    desvio=devp(est)
    est_atual=sum(est)/len(est)
    if printar==True:
        print('Estimativa=',str(round(est_atual,5))+'\nDev. padrão='+str(round(desvio,5))+'\nAgulhas='+str(n)+'\n-----------------------------')
    return(est_atual,desvio)

def area(precisao=0.01,tentativas=100,printar=True):
    n=1000
    desvio=precisao
    while desvio>precisao/1.96:
        est_atual,desvio=estimativa(n,tentativas,printar)
        n*=2
    return est_atual
