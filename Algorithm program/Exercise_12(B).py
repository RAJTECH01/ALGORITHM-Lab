import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    return quicksort(left) + [pivot] + quicksort(right)

def measure_time(n, num_repeats):
    times = []
    for _ in range(num_repeats):
        arr = [random.randint(0, 1000000) for _ in range(n)]
        start_time = time.time()
        quicksort(arr)
        end_time = time.time()
        times.append(end_time - start_time)  # Append time inside loop
    
    return sum(times) / len(times)  # Return average time

if __name__ == "__main__":
    num_repeats = 10
    max_n = 10000
    step_size = 100
    ns = range(0, max_n + step_size, step_size)
    times = []

    for n in ns:
        if n == 0:
            times.append(0)
        else:
            times.append(measure_time(n, num_repeats))

    print(times)
