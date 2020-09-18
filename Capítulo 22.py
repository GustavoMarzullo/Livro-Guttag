import matplotlib.pyplot as plt
import numpy as np

def distminkowski(v1,v2,p):
    '''Assume que v1 e v2 são vetores de mesmo tamanho.\nRetorna a distância de
Minkowski de ordem p entre v1 e v2.'''
    dist=0.0
    for i in range(len(v1)):
        dist+=abs(v1[i]-v2[i])**p
    return dist**(1/p)

class animal(object):
    def __init__(self,nome,caracteristicas):
        '''Nome é uma string e caracteristicas uma lista de números.'''
        self.nome=nome
        self.caracteristicas=np.array(caracteristicas)
    def qualnome(self):
        return self.nome
    def quaiscaracteristicas(self):
        return self.caracteristicas
    def distancia(self,other):
        '''Retorna a distância euclidiana.'''
        return distminkowski(self.quaiscaracteristicas(),other.quaiscaracteristicas(),2)
    def __str__(self):
        return '<'+str(self.nome)+','+str(self.caracteristicas)+'>'
    
def comparar_animais(animais,precisao):
    '''Assume que animais é uma lista de animais e precisão int>=0.
Faz uma tabela de distância euclidiana entre cada animal'''
    valorcolunas=[]
    for i in animais:
        valorcolunas.append(i.qualnome())
    valorlinhas=valorcolunas[:]
    valores=[]
    for a1 in animais:
        linha=[]
        for a2 in animais:
            if a1==a2:
                linha.append('--')
            else:
                dist=a1.distancia(a2)
                linha.append(str(round(dist,precisao)))
        valores.append(linha)
    tabela=plt.table(rowLabels=valorlinhas,
                       colLabels=valorcolunas,
                       cellText=valores,
                       cellLoc='center',
                       loc='center',
                       colWidths = [0.2]*len(animais))
    tabela.scale(1, 2.5)
    plt.show()
        
#>>> rattlesnake = animal('rattlesnake', [1,1,1,1,0])
#>>> boa = animal('boa\nconstrictor', [0,1,0,1,0])
#>>> dartFrog = animal('dart frog', [1,0,1,0,4])
#>>> animais=[rattlesnake, boa, dartFrog]
#>>> comparar_animais(animais,3)
