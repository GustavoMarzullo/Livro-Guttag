def taxasucesso(sucesso,falha):
    try:
        x= sucesso/falha
        print(x)
    except ZeroDivisionError:
        print('Divisão por zero')
    
def pripar(L):
    for i in L:
        if i%2==0:
            return i
    raise ValueError('Sem primos.')

def getRatios(vect1, vect2):
    '''Assume que vetor1 e vetor2 são vetores com o mesmo tamanho.
Retorna uma lista com os valores válidos de vetor[i]/vetor2[i]'''
    ratios=[]
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios
