import random
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def test_merge_sort(n):
    arr = [random.randint(1, 100) for _ in range(n)]
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    ns = [10, 100, 1000, 10000, 100000]
    times = []

    for n in ns:
        t = test_merge_sort(n)
        times.append(t)
        print(f"Merge sort took {t:.6f} seconds to sort {n} elements.")

    plt.plot(ns, times, 'o-')
    plt.xlabel('Number of elements (n)')
    plt.ylabel('Time taken (s)')
    plt.title('Merge Sort Time Complexity')
    plt.show()
