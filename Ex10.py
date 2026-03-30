def encrypt(x, shift):
    for i in x:
        temp = ord(i)
        if (temp >= 122):
            temp = 96
        temp = temp + shift
        temp = chr(temp)
        print(temp, end=" ")
    print()

def decrypt(x, shift):
    for i in x:
        temp = ord(i)
        temp = temp - shift
        if (temp <= 97):
            temp = 126
        temp = temp - shift
        temp = chr(temp)
        print(temp, end=" ")
    print()


x = str(input("Wpisz"))
print()

encrypt(x, 4)
decrypt(x, 4)


