
def bubble_sort(arr):
    len = len(arr)
    bound = len - 1
    for i in range(, len):
        tmp_bound = 0
        swap = false
        for j in range(1, bound):
            if (arr[j] > arr[j + 1]):
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                tmp_bound = j
                swap = true
        bound = tmp_bound

        if swap:
            break

    return arr

