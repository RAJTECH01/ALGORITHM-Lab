def find_max_min(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]
    else:
        mid = len(arr) // 2
        left_max, left_min = find_max_min(arr[:mid])
        right_max, right_min = find_max_min(arr[mid:])
        return max(left_max, right_max), min(left_min, right_min)

# Example usage
arr = [3, 1, 5, 2, 9, 7]
max_num, min_num = find_max_min(arr)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
