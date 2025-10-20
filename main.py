try:
    x = float(input("Podaj licby"))
    pole = 3.1415 * x * x
    print(f" {x} licba, {3.1415 * x * x} pole")
    print(f"{pole} pole")
except:
    x = "Nie liczba"
    print(x)