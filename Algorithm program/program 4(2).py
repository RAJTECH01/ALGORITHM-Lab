import matplotlib.pyplot as plt
import random
import time

# Heapify a subtree rooted with node i
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # Left child
    r = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # Check if right child exists and is greater than the largest
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Swap if necessary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Heapify the affected subtree

# Heap Sort function
def heapSort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Generate a list of n random numbers
def generateList(n):
    return [random.randint(1, 1000) for _ in range(n)]

# Measure the time required to sort a list of n elements
def measureTime(n):
    arr = generateList(n)
    start_time = time.perf_counter()  # More accurate timing
    heapSort(arr)
    end_time = time.perf_counter()
    return end_time - start_time

# Plot a graph of the time required to sort a list of n elements
def plotGraph(nList):
    timeList = [measureTime(n) for n in nList]

    plt.plot(nList, timeList, 'o-', label="Heap Sort Time")
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Heap Sort Performance')
    plt.xscale('log')  # Log scale for better visualization
    plt.yscale('log')
    plt.grid(True)
    plt.legend()
    plt.show()

# List of input sizes to test
nList = [100, 500, 1000, 2000, 5000, 10000]
plotGraph(nList)
