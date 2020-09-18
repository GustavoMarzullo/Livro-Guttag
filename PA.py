#progressão aritimética
def a_n(n,a1,r):
    '''Assume que os 3 termos inseridos são números inteiros'''
    an=a1+(n-1)*r
    return an 
def sa_n(n,a1,r):
    '''Assume que os 3 termos inseridos são números inteiros'''
    soma=((a1+a_n(n,a1,r)*n)/(2))
    return soma
    
