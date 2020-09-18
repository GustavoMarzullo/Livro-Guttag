def raiz(x):
    erro=0.01
    est=0
    numint=0
    while abs(est**2-x)>erro:
        numint+=1
        est=est+erro
    print('A raiz quadrada de '+str(x)+' é ' + str(est))
    print('Número de tentativas: '+str(numint))
