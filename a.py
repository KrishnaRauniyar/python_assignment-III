# Bubble Sort


def bubble_Sort(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


l = [1, 10, 15, 95, 65, 35, 100, 55]
bubble_Sort(l)
print ("Sorted array is:")
for i in range(len(l)):
    print("%d" %l[i])
