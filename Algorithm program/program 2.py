import random
import time
import matplotlib.pyplot as plt

def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return -1

def test_binary_search_recursive():
    n_values = [10, 100, 1000, 10000, 100000]
    time_values = []

    for n in n_values:
        arr = sorted(random.randint(1, n) for _ in range(n))
        x = random.randint(1, n)

        start_time = time.time()
        result = binary_search_recursive(arr, 0, n - 1, x)
        end_time = time.time()

        time_taken = end_time - start_time
        time_values.append(time_taken)

        if result == -1:
            print(f"Element {x} not found in the array")
        else:
            print(f"Element {x} found at index {result}")

        print(f"Time taken to search in array of size {n}: {time_taken:.6f} seconds")
        print("=" * 50)

    # Plotting outside the loop
    plt.plot(n_values, time_values, marker='o', linestyle='--', color='b', label="Recursive Binary Search")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Size of Array")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Recursive Binary Search Performance")
    plt.legend()
    plt.grid(True)
    plt.show()

test_binary_search_recursive()
