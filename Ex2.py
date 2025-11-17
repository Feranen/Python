ilosc = int(input("Dlugosc tabeli"))


print("    | ", end="")
for i in range(1, ilosc + 1):
    print(f"{i:4}", end="")

print()
print("-------------------")
for i in range(1, ilosc + 1):
    print(f"{i:3} | ", end="")
    for c in range(1, ilosc + 1):
        print(f"{i * c:4}", end="")
    print()
    
