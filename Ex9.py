import random
def min(list):
    n = len(list)
    min_index = list[0]
    for i in range(0, n):
        if list[i] < min_index:
            min_index = list[i]
    return min_index
def max(list):
    n = len(list)
    max_index = list[0]
    for i in range(0, n):
        if list[i] > max_index:
            max_index = list[i]
    return max_index
def avg(list):
    n = len(list)
    avg = list[0]
    for i in range(0, n):
        avg = avg + list[i]
    avg = avg / n
    return avg
def geo(list):
    n = len(list)
    geo = list[0]
    for i in range(0, n):
        geo = geo * list[i]
    geo = geo ** (1/n)
    return geo
def med(list):
    n = len(list)
    s = sorted(list)
    if n % 2 == 1:
        return s[n // 2]
    else:
        return (s[n // 2] + s[n // 2 - 1]) / 2



list = [random.randint(1,1000) for _ in range(10)]

print(list)

print(min(list))
print(max(list))
print(avg(list))
print(geo(list))
print(med(list))