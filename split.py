inp = input("Write text: ").split()
print(inp)
i = 0
dict = {}
for word in inp:
    dict[word] = 0


for word in inp:
    if word in dict:
        dict[word] = dict[word] + 1

max_val = 0
max_name = ""
for key in dict:
    if max_val < dict[key]:
        max_val = dict[key]
        max_name = key

print(max_name, max_val)

print(dict)

