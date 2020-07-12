#  Interpolation Search


def interpolationSearch(arr, n, x):
    lo = 0
    hi = (n - 1)
    while lo <= hi and arr[lo] <= x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


arr = [1, 10, 15, 95, 65, 35, 100, 55]
n = len(arr)

x = 55
index = interpolationSearch(arr, n, x)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")


