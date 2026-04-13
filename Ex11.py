def encrypt(input, dict):
    output = ""
    for i in input:
        n = dict[i]
        output += n
    return output

def decrypt(input, dict):
    output = ""
    for i in input:
        n = dict[i]
        output += n
    return output

dict = {
    "A": "1",
    "B": "9",
    "C": "8",
    "D": "A",
    "E": "f",
    "F": "p",
    "G": "L",
    "H": "d",
    "I": "2",
    "J": "7",
    "K": "T",
    "L": "w",
    "M": "o",
    "O": "a",
    "P": "0",
    "Q": "i",
    "R": "s",
    "S": "m",
    "T": "M",
    "U": "]",
    "V": "|",
    "W": "ô",
    "X": "Ä",
    "Y": "◄",
    "Z": "#",
    " ": "U"
}

rev = {}

for k in dict:
    rev[dict[k]] = k

input = "HELLO WORLD"
dec = "dfwwaUôaswA"

print(encrypt(input,dict))
print(decrypt(dec,rev))