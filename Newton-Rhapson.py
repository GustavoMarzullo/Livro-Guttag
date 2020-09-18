#método de newton-rhapson
#achar a raíz da equação f(x)=x^2-24
c=24
erro = 0.01
est=c/2
tentativas=0
while est**2 - c >= erro:
    tentativas+=1
    est = est -(est**2 -24)/(2*est)
print('A raíz é ' + str(est))
print('Número de tentativas: ' + str(tentativas))

