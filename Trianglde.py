def pascal(height):
    t = []

    for i in range(0, height):
        row = [1] * (i + 1)
        for ro in range(1, i):
            row[ro] = t[i-1][ro - 1] + t[i - 1][ro]
        t.append(row)
    for i in range(1, height):
        print(" " * (height-i), t[i])

height = 10
print(pascal(height))
        # print(" " * (height-i), "1", lastRow[0] * (i - 1) end="")
