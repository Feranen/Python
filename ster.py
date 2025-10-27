# Instrukcje sterujace

# and, or, not
warunek1 = True

a = 1
b = 2
c = 8

if (a > b and a != c) or (a < b and b == c):
    print("Warunek spelniony")
else:
    print("Nie")

number = int(input("Podaj liczbe "))

if number == 0:
    print("Liczba = 0")
elif number > 0:
    print("Liczba wieksza 0")
else:
    print("Liczba mniejsza od zera")

rok = int(input("Podaj rok "))
if rok < 0:
    print(".......")
elif rok <= 2:
    print("niemowlia")
elif rok < 10:
    print("Dziecko")
elif rok < 18:
    print("nastolatek")
elif rok == 18:
    print("Pelnoletni")
else:
    print("Dorosla")