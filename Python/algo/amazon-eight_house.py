# Autho: Cj Galindo
# Amazon Coding Challenge
# Eight houses
# O (n)
def cellCompete(states, days):
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
    states.insert(0,0)
    states += [0]
    
    itera = days
    output = []
    
    for i in range(1, len(states) - 1): 
        if states[i - 1] == 1 and states[i + 1] == 1:
            output.append(0)
        elif states[i - 1] == 0 and states[i + 1] == 0:
            output.append(0)
        else:
            output.append(1)

    itera -= 1
    if itera:
        output = cellCompete(output, itera)
        
    return output
    

print(cellCompete([1,0,0,0,0,1, 0, 0],1))
print(cellCompete([1,1,1,0,1,1,1,1],2))
