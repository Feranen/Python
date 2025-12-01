def hello(name):
    print(f"Hello, {name}")

def dodaj(a, b = 1):
    return a + b


hello("Fyrka")

wynik = dodaj(3,5)

print(dodaj(1), wynik)