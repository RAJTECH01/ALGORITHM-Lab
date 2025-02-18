import random

# Function to partition the array around a pivot
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to find the k-th smallest element using randomized select
def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    index = partition(arr, low, high)
    
    if k == index:
        return arr[k]
    elif k < index:
        return randomized_select(arr, low, index - 1, k)
    else:
        return randomized_select(arr, index + 1, high, k)

# Testing the function
arr = [9, 4, 2, 7, 3, 6]
k = 3
n = len(arr)
result = randomized_select(arr, 0, n - 1, k - 1)  # k-1 because the index is 0-based
print(f"The {k}th smallest number is: {result}")
