import matplotlib.pyplot as plt
import random
import time

# Insertion Sort Algorithm
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate a list of n random numbers
def generateList(n):
    return [random.randint(1, 1000) for _ in range(n)]

# Measure the time required to sort a list of n elements
def measureTime(n):
    arr = generateList(n)
    start_time = time.perf_counter()  # More accurate for timing small operations
    insertionSort(arr)
    end_time = time.perf_counter()
    return end_time - start_time

# Plot a graph of the time required to sort a list of n elements
def plotGraph(nList):
    timeList = [measureTime(n) for n in nList]
    
    plt.plot(nList, timeList, 'o-', label="Insertion Sort Time")
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Insertion Sort Performance')
    plt.xscale('log')  # Log scale for better visualization
    plt.yscale('log')
    plt.grid(True)
    plt.legend()
    plt.show()

# List of input sizes to test
nList = [100, 500, 1000, 2000, 5000, 10000]
plotGraph(nList)
