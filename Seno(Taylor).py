import numpy
import pylab
import sys
sys.setrecursionlimit(1500000000)
#------------------------------------------------------------------------       
def fatorial(n):  #definindo uma função fatorial
        '''Função fatorial n!'''
        if n<0:
                print('Erro')
        elif n==0:
                return 1
        elif n==1:
                return n
        else:
                return n*fatorial(n-1)
#------------------------------------------------------------------------       
def sin(x,erro=0.0001):  #definindo a função seno
        L=[]
        i=0
        numtermos=0
        termo= erro +1 #defini um valor aleatório para o valor termo entrar no loop
        while abs(termo) >= erro:
            termo=((-1)**i)*(x**(2*i+1)/(fatorial(2*i+1))) #série de taylor para o sin(x)
            L.append(termo)
            i+=1
            numtermos+=1
        seno=sum(L)
        senoarr=round(seno,(len(str(int(1/erro)-1)))) #método estranho que inventei para arredondar
        print(str((senoarr))+'+/-'+str(erro))
        print('Número de termos='+str(numtermos))
        return L
#------------------------------------------------------------------------       
def sinG(x,Erro=0.001):  #definindo uma função seno para valores em graus
    '''retorna o valor de seno(graus)'''
    x=(numpy.pi*x)/180
    sin(x,Erro)

