#bisection search para a raiz quadrada
def raiz(x,exp=2,erro=0.0001):
    assert x>=0 and exp>0 and erro>0, 'Erro.'
    tentativas=0
    inf=0
    sup=max(1,x)
    est=(inf+sup)/2
    while abs(est**exp-x) >= erro:
        tentativas +=1
        if est**exp>x:
            sup=est
        else:
            inf=est
        est=(inf+sup)/2
    print('A raiz de '+str(x)+' é ' + str(est))
    print('Número de tentativas: '+str(tentativas))
