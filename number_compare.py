def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    # we want to return a string
    # we want to return 'Numbers are equal' if a and b are equal
    # we want to return 'First is greater' if a is greater than b
    # we want to return 'Second is greater' if b is greater than a
    if a > b:
        return 'First is greater'
    elif b > a:
        return 'Second is greater'
    else:
        return 'Numbers are equal'
    