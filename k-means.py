import numpy as np

class catalisador(object):
    def __init__(self,nome,caracteristicas):
        self.nome=nome
        self.caracteristicas=np.array(caracteristicas)
    def nome(self):
        return self.nome
    def caracteristicas(self):
        return self.caracteristicas
    def dimensao(self):
        return len(self.caracteristicas)
    def distancia(self,other):
        return distminkowski(self.caracteristicas,other.caracteristicas,2)


class k_means:
    def __init__(self,k=2,tol=0.001,iter_max=300):
        self.k=k
        self.tol=tol
        self.iter_max=iter_max

    def fit(self,data):
        self.centroid={}
        for i in range(self.k):
            self.centroids[i]=data[i].caracteristicas

        for i in range(self.iter_max):
            self.classificacoes={}
            for i in range(self.k):
                self.classificacoes[i]=[]
            for caracateristicass in data:
                distancias=[np.linalg.normal(
                 

    def predict(self,data):
        pass






#definindo os catalisadores
ahn=catalisador('Ahn',[425,9.468])
gonzales=catalisador('Gonzales',[320,1.8])
larina=catalisador('Larina',[375,1.3])
lewandowski=catalisador('Lewandowski',[325,0.3])
li=catalisador('Li',[450,4.1])
baerdemaker_2015=catalisador('Baerdemaker_2015',[360,0.64])
pomazala_2016=catalisador('Pomazala_2016',[400,0.938])

#botando tudo num vetor
catalisadores=[ahn,gonzales,larina,lewandowski,li,baerdemaker_2015,pomazala_2016]
