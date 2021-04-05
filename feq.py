from math import isclose as _isclose
from numpy.linalg import solve
from chempy import balance_stoichiometry as _balancear
from molmass import Formula as _Formula

def igual(a,b):
    '''Função math.isclose com rel_tol=0.05'''
    return _isclose(a,b,rel_tol=0.05)
    
def mm(A):
	'''Retorna a massa molar do composto A'''
    
	f = _Formula(A)
	return f.mass

def _separar(reacao):
    '''
    Input: 
        'C2H6 + O2 --> CO2 + H2O'
    
    Output:
        (['C2H6','O2'],['CO2','H2O'])

    '''
    
    #separando a string
    reag,prod=reacao.split('-->')
    reag=reag.split('+')
    prod=prod.split('+')
    
    #tirando os espaços em branco
    for i in range(len(reag)):
        reag[i]=reag[i].strip()
    for i in range(len(prod)):
        prod[i]=prod[i].strip()
    
    return reag,prod
        
def balancear(reacao):
    '''
    Input:
        'C2H6 + O2 --> CO2 + H2O'
        
    Output:
        '2 C2H6 + 7 O2 --> 4 CO2 + 6 H2O'
    '''
    
    #separando a string
    reag,prod=_separar(reacao)
    
    #balanceando a equação
    reag,prod=_balancear(reag,prod,underdetermined=None)
    
    #formando a string para printar
    out=''
    for i in reag:
        nu=str(reag[i])
        if int(nu)==1:
            nu=''
        out+=nu+ ' ' +str(i)+' + ' 
    out=out[:-3] #tirando o último ' + '
    out+= ' --> ' 
    for i in prod:
        nu=str(prod[i])
        if int(nu)==1:
            nu=''
        out+=nu+ ' ' +str(i)+' + '
    out=out[:-3]
    if out[0]==' ': #tirando o espaço em branco no início (só acontece quando o primeiro nu dos reagentes é igual a 1)
    	out=out[1:]
    	
    print(out)


