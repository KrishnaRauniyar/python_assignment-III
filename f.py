# Binary Search


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


arr = [1, 10, 15, 95, 65, 35, 100, 55]
x = 10
result = binary_search(arr, x)
if result != -1:
    print("Index of element is : ", str(result))
else:
    print("Element is not present in array")
