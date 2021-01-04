
def dif(f,x,h=1e-5):
    try:
        derivada=(-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
        return derivada
    except NameError:
        print('A função f não foi definida.')
def dif2(f,x,h=1e-5):
    try:
        derivada=(-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h**2)
        return derivada
    except NameError:
        print('A função f não foi definida.')

print(dif(lambda x: x**2,2))