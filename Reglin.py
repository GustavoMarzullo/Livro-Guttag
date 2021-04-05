from statsmodels.api import add_constant, OLS
from numpy import polyfit, poly1d, corrcoef, array
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText


class _afim(object):
    '''Classe feita para se definir uma função linear'''
    def __init__(self,a,b,r_2):
        self.a=a
        self.b=b
        self.r_2=r_2
        
    def __repr__(self):
        if self.b <0:
            return 'y = '+ str(round(self.a,5))+ 'x'+' - '+ str(round(-self.b,7))
        else:
            return 'y = '+ str(round(self.a,5))+ 'x'+' + '+ str(round(self.b,7))
    
    def __str__(self):
        if self.b <0:
            return 'y = '+ str(round(self.a,5))+ 'x'+' - '+ str(round(-self.b,7))
        else:
            return 'y = '+ str(round(self.a,5))+ 'x'+' + '+ str(round(self.b,7))
        
    def y(self,x_i):
        '''Retorna o valor de y_i em dado x_i'''
        return self.a*x_i+self.b
    
    def x(self,y_i):
        '''Retorna o valor de x_i em dado y_i'''
        return (y_i-self.b)/self.a
    
    def raiz(self):
        '''Retorna a raiz da função'''
        return self.x(0)
    
    def coef(self):
        '''Retorna os coeficientes'''
        return self.a,self.b
    
    def r2(self):
        '''Retorna o r^2'''
        return self.r_2


def reg(X,Y):
    '''Retorna uma classe função a partir da função reglin'''
    return _afim(*reglin(X,Y,True))


def reglin(X,Y,r2=False):
    '''Se verbose=True :retorna os coeficientes a e b e o r^2.
    Se verbose=False retorna os coeficientes a e b'''
    a,b = polyfit(X, Y, 1)
    correlation_matrix = corrcoef(X, Y)
    correlation_xy = correlation_matrix[0,1]
    r_2 = correlation_xy**2
    if r2:
        return a,b,r_2
    else:
        return a,b


def sumario(X,Y):
    '''Regressão mais completa da biblioteca statsmodels.api.'''
    X_sm=add_constant(X)
    results = OLS(Y, X_sm).fit()
    print(results.summary())


def plotar(X,Y,algarismos=6,title=' ',xlabel=' ',ylabel=' ',labelsize=12,titlesize=14,annotate_size= 10,marker='yo',verbose=True):
    '''Faz um gráfico X versus Y.'''

    coef = polyfit(X, Y, 1)
    poly1d_fn = poly1d(coef)
    fig, ax = plt.subplots()
    ax.plot(X,Y, marker, X, poly1d_fn(X), '--k',color='black')
    plt.title(title,size=titlesize)
    plt.xlabel(xlabel,size=labelsize)
    plt.ylabel(ylabel,size=labelsize)

    if verbose: #anotação

        #calculando os coeficientes
        a,b=coef[0],coef[1]
        formatador="{0:."+str(algarismos)+"g}"
        
        #fazendo o r^2
        correlation_matrix = corrcoef(X, Y)
        correlation_xy = correlation_matrix[0,1]
        r_2 = round(correlation_xy**2,4)

        #configurando para plotar
        if b!=0:
            if b > 0:
                sinal = ' + '
            else:
                sinal= ' - '
            if a>=0:
                at=AnchoredText('y = '+formatador.format(a)  +'x'+ sinal +formatador.format(abs(b))+'\nr$^2$'+' = '+str(r_2),loc='upper left',prop=dict(size=annotate_size))
            else:
                at=AnchoredText('y = '+formatador.format(a)  +'x'+ sinal +formatador.format(abs(b))+'\nr$^2$'+' = '+str(r_2),loc='upper right',prop=dict(size=annotate_size))
                
        else:
            if a>=0:
               at= AnchoredText('y = '+formatador.format(a)  +'x'+ '\nr$^2$'+' = '+str(r_2),loc='upper left',prop=dict(size=annotate_size))
            else:
                at= AnchoredText('y = '+formatador.format(a)  +'x'+'\nr$^2$'+' = '+str(r_2),loc='upper right',prop=dict(size=annotate_size))
                
        at.patch.set_boxstyle("round,pad=0.,rounding_size=0.1")
        ax.add_artist(at)
        
        
def curva(X,Y,func,title=' ',xlabel=' ',ylabel=' ',labelsize=12,titlesize=14,marker='yo'):
    '''Faz regressão a partir da função func definida pelo usuário.
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
    
    Precisa-se definir a posição da anotação manualmente com o comando plt.annotate'''
    
    if type(X)!="<class 'pandas.core.series.Series'>" and type(X) !="<class 'numpy.ndarray'>":
        X=array(X)
    if type(Y)!="<class 'pandas.core.series.Series'>" and type(Y) !="<class 'numpy.ndarray'>":
        Y=array(Y)  
        
    popt, pcov = curve_fit(func, X, Y)
    plt.plot(X, Y, marker,color='black')
    plt.plot(X, func(X, *popt),'--k',color='black')
    plt.title(title,size=titlesize)
    plt.xlabel(xlabel,size=labelsize)
    plt.ylabel(ylabel,size=labelsize)
    return popt    
 

def maplist(func,X):
    '''Função map mas retornando um array'''
    return array(list(map(func,X)))
