import random

#rozmiar = int(input("Podaj wysokosc piramidy"))

#for i in range(1, rozmiar+1):
    
#    print(" " * (rozmiar - 1 ),"#" * i)


#losowe = random.randint(1, 100)
#proba = 0
#
#print("Zgadnij liczbe")
#
#while True:
#    liczba  = int(input("Podaj liczbe: "))
#    proba += 1
#    if liczba < losowe:
#        print("Liczba jest za mala")
#
#    if liczba > losowe:
#        print("liczba jest za duza")
#
#    if liczba == losowe:
#        print(f"Poprawne, liczba = {losowe}, {proba} prob")
#        break

rozmiar = int(input("Podaj wysokosc piramidy"))
for i in range(1, rozmiar + 1):
    print(" " * (rozmiar-i), "#" * (2 * i - 1))
