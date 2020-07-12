# Insertion Sort


def insertion_Sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


l = [1, 10, 15, 95, 65, 35, 100, 55]
insertion_Sort(l)
print("Sorted array is:")
for i in range(len(l)):
    print("%d" %l[i])
