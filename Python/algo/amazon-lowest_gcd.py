  """
    The greatest common divisor (GCD), also called highest common factor
    (HCF) of N numbers in the largest positive integer that divides all numbers without giving a remainder.

    Write an algorithm to determine the GCD of N positive integers.
    Input
    The input to the function/method consists of two arguments - num, an integer representing the number of positive integers (N).
    arr, a list of positive integers.
    Output
    Return an integer representing the GCD of the given positive integers.

    Example
    Input
    num = 5
    arr = [2,4,6,8,10]
    Output:
    2
    Explanation
    The largest positive integer that divides all possible integers 

    Example
    Input:
    num. 5
    arr = [2,4,6,8,10]
    Output
    2
    Explanation:
    The largest positive integer that divides all the positive integers 2,4,6,8,10
    without a remainder is 2
    """
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
