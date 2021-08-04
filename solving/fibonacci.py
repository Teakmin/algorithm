def fib(n):
    if n == 0 or n==1 : return n # fib(0) = 1, fib(1) =1
    return fib(n - 1 ) + fib(n - 2) # fib(n) = fib(n-1) + fib(n-2)


print(fib(5))
print(fib(4))
print(fib(3))