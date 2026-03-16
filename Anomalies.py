import random
def avg(list):
    n = len(list)
    avg = 0
    for i in range(0, n):
        avg = avg + list[i]
    avg = avg / n
    return avg
def med(list):
    n = len(list)
    s = sorted(list)
    if n % 2 == 1:
        return s[n // 2]
    else:
        return (s[n // 2] + s[n // 2 - 1]) / 2
def anomalyDetection(list):
    median = med(list)
    anomaly = []
    anomalyRatio = []
    for x in list:
        ratio = (x / median)
        if (ratio > 2 or ratio < 0.5):
            print(f"Anomaly detected: {x}, its ratio is whooping {ratio}" )
    #         anomaly.append(x)
    # return anomaly




list = [random.randint(1,1000) for _ in range(10)]
list1 = [2, 5, 5, 7, 1000]

print(list)
print(sorted(list))
print(avg(list))
print(med(list))
anomalyDetection(list)
# print(anomalyDetection(list))