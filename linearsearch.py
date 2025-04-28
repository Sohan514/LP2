def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 3, 8, 6, 7]
target = 6
result = linear_search(arr, target)

print(f"Element found at index {result}" if result != -1 else "Element not found")
