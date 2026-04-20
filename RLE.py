def RLE(input):
    output = ""
    counter = 1
    for i in range(1, len(input)):
        if input[i-1] == input[i]:
            counter +=1
        else:
            output += input[i-1]
            output += str(counter)
            counter = 1
    output += input[-1]
    output += str(counter)
    return output


input = "AAABBBDDD"

print(RLE(input))