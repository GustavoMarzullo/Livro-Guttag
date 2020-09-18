print('Algoritimo para encontrar as raízes de uma equação do segundo grau (ax^2+bx+c).')
def raiz(a,b,c):
    delta=(b*b)-4*a*c
    if delta > 0:
        x1= (-b + (delta)**(0.5))/(2*a)
        x2= (-b - (delta)**(0.5))/(2*a)
        print ('As raízes são:', x1,'e',  x2,'.')
    elif delta == 0:
        x3= (-b)/(2*a)
        print('A raíz é:',x3,'.')
    elif delta < 0:
        print('Não há raízes reais')

