def magicSquare(square):
    if len(square) < 1:
        raise EmptySquare('A empty square matrix is given')
    
    constantSum = 0
    for element in square[0]:
        constantSum += element

    for line in square:
        sum = 0
        for element in line:
            sum += element

        if sum != constantSum:
            return False
    return True
