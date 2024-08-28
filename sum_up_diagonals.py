def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # matrix is a square list of lists
    # we want to return a number
    # we want to return the sum of the diagonals of the matrix
    # we can get the sum of the top-left to bottom-right diagonal by adding matrix[i][i]
    # we can get the sum of the bottom-left to top-right diagonal by adding matrix[i][-1-i]
    total = 0
    
    for i in range(len(matrix)):
        total += matrix[i][i] + matrix[i][-1-i]
        
    return total
    # When we run the doctests, we get this:
    # $ python3 -m doctest sum_up_diagonals.py