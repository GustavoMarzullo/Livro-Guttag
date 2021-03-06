#Abordagem da bisseção para achar o log
#log(x) = y <=> 10^y=x

def log(x,erro=1e-5):
        numint=0
        inf=0
        sup=x
        y=(inf+sup)/2
        if x>= 1:
                while abs(10**y-x)>=erro:
                        numint+=1
                        if 10**y>x:
                                sup=y
                        else:
                                inf=y
                        y=(inf+sup)/2
                print('O log de '+str(x)+ ' é igual a ' + str(y)+'.')
                print('Nº de iterações='+str(numint))
        elif x>0 and x<1:
                        x=x**-1
                        sup=x
                        y=(inf+sup)/2
                        while abs(10**y-x)>=erro:
                                numint+=1
                                if 10**y>x:
                                        sup=y
                                else:
                                        inf=y
                                y=(inf+sup)/2.0
                        y=-y
                        x=x**-1
                        print('O log de '+str(x)+ ' é igual a ' + str(y)+'.')
                        print('Nº de iterações='+str(numint))
                
        elif x<0:
                print('Não existe log de número negativo.')
        else:
                print('Não existe o log de zero.')

