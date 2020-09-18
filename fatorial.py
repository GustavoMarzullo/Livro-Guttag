def fatorialI(n):
    resultado=1
    while n>1:
        resultado=resultado*n
        n-=1
    return(resultado)

def fatorialR(n):
    if n==1:
        return n
    else:
        return n*fatorialR(n-1)

def fib(n):
    global numfibcalls
    numfibcalls +=1
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        

def testefib(n):
    global numfibcalls
    numfibcalls = 0
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
        print('fib called', numfibcalls, 'times.')
#fib(4)+fib(3) = fib(3) + fib(2) + fib(2) + fib(1) 
