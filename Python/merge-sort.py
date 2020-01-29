import math

def merge_sort(arr):
    count = len(arr)

    if count == 1:
        return arr

    mid = math.floor(count / 2)

    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    arr = []
    len_left = len(left)
    len_right = len(right)
    index_left, index_right = 0,0

    while index_left < len_left and index_right < len_right:
        if left[index_left] < right[index_right]:
            arr.append(left[index_left])
            index_left += 1
        else:
            arr.append(right[index_right])
            index_right +=1
    
    while index_left < len_left:
        arr.append(left[index_left])
        index_left += 1

    while index_right < len_right:
        arr.append(right[index_right])
        index_right += 1
    
    return arr

print(merge_sort([9,8,7,5,3,6,2,1,4]))