# Linear Search


def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [1, 10, 15, 95, 65, 35, 100, 55]
print(search(arr, 95))