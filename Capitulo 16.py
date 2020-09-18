import random
def jogardado():
    return random.choice([1,2,3,4,5,6])

def checarPascal(n):
    ganhos=0
    for i in range(n):
        for i in range(24):
            d1=jogardado()
            d2=jogardado()
            if d1==6 and d2==6:
                ganhos+=1
                break
    print('Probabiliade de ganhar=',ganhos/n)

class craps(object):
    def __init__(self):
        self.passwin,self.passloss=0,0
        self.dpwin,self.dploss,self.dppushes=0,0,0
    def play(self):
        throw=jogardado()+jogardado()
        if throw==7 or throw==1:
            self.passwin+=1
            self.dploss+=1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passloss+=1
            if throw==12:
                self.dppushes+=1
            else:
                self.dpwin+=1
        else:
            point=throw
            while True:
                throw=jogardado()+jogardado()
                if throw==point:
                    self.passwin+=1
                    self.dploss+=1
                    break
                elif throw==7:
                    self.passloss+=1
                    self.dpwin+=1
                    break
    def passresults(self):
        return (self.passwin,self.passloss)
    def dpresults(self):
        return (self.dpwin,self.dploss,self.dppushes)
#aleatórios
def devp(X):
    media=sum(X)/len(X)
    somatorio=0.0
    for i in X:
        somatorio+=(i-media)**2
    return (somatorio/len(X))**0.5

#achar pi
def jogar_agulhas(n):
    dentro=0
    for agulhas in range(1,n+1):
        x=random.random()
        y=random.random()
        if(x**2+y**2)**0.5 <=1:
            dentro+=1
    return 4*(dentro/n)

def estimativa(n,tentativas,printar=True):
    est=[]
    for i in range(tentativas):
        pi_est=jogar_agulhas(n)
        est.append(pi_est)
    desvio=devp(est)
    est_atual=sum(est)/len(est)
    if printar==True:
        print('Estimativa=',str(round(est_atual,5))+'\nDev. padrão='+str(round(desvio,5))+'\nAgulhas='+str(n)+'\n-----------------------------')
    return(est_atual,desvio)

def pi(precisao=0.01,tentativas=100,printar=True):
    n=1000
    desvio=precisao
    while desvio>precisao/1.96:
        est_atual,desvio=estimativa(n,tentativas,printar)
        n*=2
    return est_atual

    
    
            
    
