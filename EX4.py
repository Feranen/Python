

def rysuj_kwadrat(n):
    for i in range(0,n):
        for i in range(0,n):
            print("*", end="")
        print()
rysuj_kwadrat(3)

def rysuj_trojkat(n):
    for i in range(1, n + 1):
        print(" " * (n-i), "#" * (2 * i - 1))

rysuj_trojkat(3)

def rysuj_prostokat(n,m):
        for i in range(0,n):
            for i in range(0,m):
                print("*", end="")
            print()

rysuj_prostokat(6, 8)