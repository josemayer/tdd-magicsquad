def magicSquare(square):
    value = square[0][0]
    for line in square:
        for element in line:
            if element != value:
                return False
    return True;
