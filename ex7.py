def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fibfor(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a + b
    return b

o = 10


print(fibfor(o), " Fib With for")
print("------------")
print(fib(o), " Fib With recurention")