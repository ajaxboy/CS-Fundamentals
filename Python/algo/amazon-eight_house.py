# Autho: Cj Galindo
# Amazon Coding Challenge
# Eight houses
# O (n)
def cellCompete(states, days):
    """
    Eight house, represented as cells, are arranged in a straight line. Each day
    every cell competes with its adjacent cells (neighbors). An integer value of 1 represents an active cell and a value of 0 represents an inactive cell. 
    If the neighbors on both sides of a cell are either active or inactive, the cell  becomes inactive on the next day; otherwise the cell becomes active. The two cells on each end have a single adjacent cell, so assume that the unoccupied space on the opposite side is an inactive cell. 
    Even after updating the cell state information of all cells should be updated simultaneously.

    Write an algorithm to output the state of the cell after the given number of days.
    
    Input
    The input to the function/method consist of two arguments.
    states, a list of integers representing the current state of cells;
    days an integer representing the number of days.

    Output Return a list of integers representing the state of the cell after the given number of days

    Testcase 1:
    input
    [1, 0, 0, ,0 ,0 , 1, 0, 0], 1
    Expected Return Value:
    0 1 0 0 1 0 1 0

    Testcase 2:
    [1, 1, 1, 0, 1, 1, 1, 1, 2
    Expected Output:
    0 0 0 0 0 1 1 0
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
