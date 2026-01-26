# import sys
# sys.setrecursionlimit(1500)


def silnia(n):
    if n <= 1:
        return 1
    return n * silnia(n-1)



def silniaFor(n):
    for i in range(1, n):
        n = n * i
    return n
    

o = 10

print(silniaFor(o), "With for")
print("------------")
print(silnia(o), "With recurention")