def magicSquare(square):
    if len(square) < 1:
        raise EmptySquare('A empty square matrix is given')
    
    constantSum = 0
    for element in square[0]:
        constantSum += element

    # Verify if line-sum is equal to a constant value
    for i in range(len(square)):
        sum = 0
        for j in range(len(square)):
            sum += square[i][j]

        if sum != constantSum:
            return False

    # Verify if column-sum is equal to a constant value
    for j in range(len(square)):
        sum = 0
        for i in range(len(square)):
            sum += square[i][j]
        
        if sum != constantSum:
            return False

    # Verify if main diagonal sum is equal to a constant value
    sum = 0
    for i in range(len(square)):
        sum += square[i][i]

    if sum != constantSum:
        return False

    # Verify if secondary diagonal sum is equal to a constant value
    sum = 0
    for i in range(len(square)):
        sum += square[i][(len(square) - 1) - i]

    if sum != constantSum:
        return False

    return True
