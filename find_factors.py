def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # num is a number
    # we want to return a list of numbers
    # we want to return the factors of num in increasing orderS
    n_list = [n for n in range(1, num // 2 + 1) if num % n == 0]
    
    n_list.append(num)
    
    return n_list

    # When we run the doctests, we get this:
    # $ python3 -m doctest find_factors.py
