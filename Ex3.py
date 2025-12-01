liczba = int(input("podaj liczbe"))

def kwa(liczba):
    return liczba * liczba
print(kwa(liczba))

print()
for i in range(0, liczba):
    print(kwa(liczba=i+1), "")