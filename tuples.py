# tuples - krotki
lista = [1,2,23]

slownik = {}
my_tuple = (1, "Jeden", [1,2,23])

lista[1] = 4
# my_tuple[1] = "dwa" ------ NO

#krotki bez nawiasow
my_tuple2 = 3,4,5

a = [1, 2, 3]
b = (1, 2, 3)

tmp = a
a = b
b = tmp

print(a,b)

a, b = b, a
print(a,b)