import random
import time

def count_sort(list):
    max_val = max(list)
    count = [0] * (max_val + 1)

    for num in list:
        count[num] += 1
    i = 0
    for num in range(len(count)):
        for x in range(count[num]):
            list[i] = num
            i += 1
    return list



list = [random.randint(1,1000) for _ in range(100)]

start_time = time.time_ns()
print(count_sort(list))
end_time = time.time_ns()

print(end_time - start_time, "Count Sort")