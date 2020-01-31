
def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    result = 0
    for i in range(len(arr)):
        result = getLow(result, arr[i])
    return result

def getLow(a, b):
    while b > 0:
        a, b = b, a % b
    return a


print(generalizedGCD(5, [2,3,4,5,6]))
print(generalizedGCD(5, [2,4,6,8,10]))
