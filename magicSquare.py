def magicSquare(square):
    if len(square) < 1:
        raise EmptySquare('A empty square matrix is given')

    value = square[0][0]
    for line in square:
        for element in line:
            if element != value:
                return False
    return True;
