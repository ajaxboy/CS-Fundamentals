
def bubble_sort(arr):
    count = len(arr)
    bound = count - 1
    for i in range(1, count):
        tmp_bound = 0
        for j in range(1, bound):
            if (arr[j] > arr[j + 1]):
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                tmp_bound = j
    return arr


arr = [3,6,55,23,77,44,21,33,10,5,42,11,15]

print(bubble_sort(arr))