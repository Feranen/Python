# Set - zbiory

lista = [1,1,1,1]
dict = {"klucz" : "wartosc"}
set = {1,1,2,3,4,5,5}
tuples = (1,2,3)
print(lista, dict, tuples,set)


set_a = {1,2,3}
set_b = {2,3,4}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
print(set_b - set_a)
print(set_a ^ set_b)