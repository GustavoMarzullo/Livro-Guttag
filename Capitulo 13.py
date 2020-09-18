def fib(n):
    """Assumes n is an int >= 0
Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fastfib(n,memo={}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastfib(n-1,memo)+ fastfib(n-2, memo)
        memo[n]=result
        return result
