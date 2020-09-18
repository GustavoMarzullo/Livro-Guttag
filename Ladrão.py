#1 encher por maior valor
#2 encher por menor peso
#3 encher por maior densidade de valor

class item(object): #fazendo a classe
    def __init__(self,n,v,p):
        self.nome=n
        self.peso=p
        self.valor=v
    
    def Nome(self):
        return self.nome
    def Peso(self):
        return self.peso
    def Valor(self):
        return self.valor
    def __str__(self):
        resultado='<'+self.nome+', '+str(self.valor)+', '+str(self.peso)+'>'
        return resultado
    
def valor(item):
        return item.Valor()
def peso(item):
        return item.Peso()
def densidade(item):
        return item.Valor()/item.Peso()
def peso_inverso(item):
        return 1.0/item.Peso()
    
def inserir_itens(): #botando os dados
    nomes=['relógio','pintura','rádio','vaso','livro','computador']
    valores=[175,90,20,50,10,200]
    pesos=[10,9,4,2,1,20]
    Itens=[] #vetor de dados 
    for i in range(len(valores)):
        Itens.append(item(nomes[i],valores[i],pesos[i])) #criando a classe item para cada um
    return Itens

def greedy(itens,pesomax,keyFunction):
    copia_itens=sorted(itens,key=keyFunction,reverse=True) #criando uma lista ordenando por #1, #2 ou #3 (keyFunction)
    resultado=[]
    valor_total=0.0
    peso_total=0.0
    for i in range(len(copia_itens)): #coração do código
        if peso_total+copia_itens[i].Peso() <= pesomax:
            resultado.append(copia_itens[i])
            peso_total+=copia_itens[i].Peso()
            valor_total+=copia_itens[i].Valor()
    return (resultado,valor_total)

def teste_greedy(itens,pesomax, keyFunction): #retorna o valor e os itens roubados para cada caso
    tomado,val=greedy(itens,pesomax,keyFunction) 
    print('O valor total roubado é '+str(val))
    for item in tomado:
        print(' ',item)
        
def roubo(pesomax=20): #junta o teste_greedy para cada caso em um comando só
    itens=inserir_itens()
    print('<item, valor, peso>')
    print('\nEncher por maior valor:')
    teste_greedy(itens,pesomax, valor)
    
    print('\nEncher por menor peso:')
    teste_greedy(itens,pesomax, peso_inverso)
    
    print('\nEncher por densidade de valor:')
    teste_greedy(itens,pesomax, densidade)

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].Peso() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.Peso())
        withVal += nextItem.Valor()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
    if withVal > withoutVal:
        result = (withVal, withToTake + (nextItem,))
    else:
        result = (withoutVal, withoutToTake)
        return result



    

        
