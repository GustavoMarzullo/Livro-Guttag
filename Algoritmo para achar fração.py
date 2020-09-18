#Algoritimo para representar um número não inteiro como fração.
#Meu pseudo código:
    
# 1 Multiplique o número por 2 e arredonde-o para baixo (numerador). 
# 2 Agora a fração é numerador(resultado acima)/denominador(2)
# 3 while |x-numerador/denominador| > erro:
# 4   if numerador/denominador> número:
# 5       denominador +=1
# 6   else:
# 7       numerador+=1
# 8   retornar numerador e denominador 
 
import matplotlib.pyplot as plt

def fracao(x,erro=1e-4,plotar=False,printar=False):
    '''Retorna o númerado e o demonimador respectivamente.'''
    num_iter=1
    numerador= int(x*2)
    denominador=2
    lista_erro,iteracao=[],[]
    while abs(x-numerador/denominador)>erro:
        lista_erro.append(abs(x-numerador/denominador))
        iteracao.append(num_iter)
        if numerador/denominador > x:
            denominador+=1
        else:
            numerador+=1
        if printar==True:
            print(str(num_iter), str(numerador), str(denominador), str(abs(x-numerador/denominador)))    
        num_iter+=1
    print('Número de iterações= '+str(num_iter))
    if plotar==True:
        plt.plot(iteracao,lista_erro,color='black',linestyle='--',linewidth=1,marker='o',markersize=3)
        plt.xlabel('Iteração')
        plt.ylabel('Erro absoluto')
    return numerador,denominador 
 
    