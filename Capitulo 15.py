import random
import pylab as py
#probabilidade
def jogar_dado():
    '''Escolhe aleatoriamente um valor de 1 a 6.'''
    return random.choice([1,2,3,4,5,6])

def jogarn(n):
    '''Joga um dado n vezes'''
    resultado=''
    for i in range(n):
            resultado=resultado+str(jogar_dado())
    print(resultado)

def jogar_moeda(n):
    '''Assume que n é um número natural. Retorna a razão cara/coroa da moeda.'''
    cara=0
    for i in range(n):
        if random.choice(('cara','coroa'))=='cara':
            cara+=1
    return cara/float(n)

def media_jogo(x,n):
    '''Assume que x e n são um números naturais. Retorna a média da probabilidade dar cara de x séries de n jogadas de moeda.'''
    L=0
    for i in range(x):
        tent=jogar_moeda(n)
        L+=tent
    return L/x
#estatística
def var(X):
    '''Assume que X é uma lista de números. Retorna a variância da lista'''
    media=sum(X)/len(X)
    somatorio=0.0
    for i in X:
        somatorio+=(i-media)**2
    return somatorio/len(X)

def devp(X):
    '''Assume que X é uma lista de números. Retorna o desvio-padrão da lista'''
    return (var(X))**0.5

def CV(X):
    '''Retorna o coeficiente de variação da lista X'''
    media=sum(X)/len(X)
    try:
        return devp(X)/media
    except ZeroDivisionError:
        return float('nan')
    
#15.4
def jogo_sim(n,x):
    '''x=nº de séries. n=nº de tentativas por série'''
    fracao_caras=[]
    for i in range(x):
        fracao_caras.append(jogar_moeda(n))
    media=sum(fracao_caras)/len(fracao_caras)
    dp=devp(fracao_caras)
    return(fracao_caras,media,dp)

def plotar(n,x,media,dp):
    py.title(str(x)+' séries de '+str(n)+' jogadas')
    py.xlabel('Fração de caras')
    py.ylabel('Número de tentativas')
    py.annotate('Média='+str(round(media,4))+ '\n DP='+str(round(dp,4)),size='x-large',xycoords='axes fraction',xy = (0.75, 0.6))

def fazerplotar(n1,n2,x):
    #primeiro gráfico
    val1,media1,dp1=jogo_sim(n1,x)
    py.hist(val1,bins=20,facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
    xmin,xmax=py.xlim()
    plotar(n1,x,media1,dp1)
    py.figure()
    py.show()
    #segundo gráfico
    val2,media2,dp2=jogo_sim(n2,x)
    py.hist(val2,bins=20,facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
    py.xlim(xmin,xmax)
    plotar(n2,x,media2,dp2)
    py.show()
    
        


    
