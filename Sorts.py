import random
import time

def current_milli_time():
    return round(time.time() * 1000)

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(1+i, n):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list






list = [random.randint(1,1000) for _ in range(100)]


print(insertion_sort(list))

start_time = time.time_ns()

print(bubble_sort(list))
end_bubble_time = time.time_ns()

selection_start_time = time.time_ns()

print(selection_sort(list))

end_time = time.time_ns()

print(end_bubble_time - start_time, "Time for bubble sort")
print(end_time - selection_start_time, "Time for selection sort")