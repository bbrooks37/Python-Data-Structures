def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    # nums is a list of numbers
    # we want to return a number
    # we want to return the sum of the floating point numbers in the list
    # we want to return 0 if there are no floating point numbers in the list
    return sum([num for num in nums if isinstance(num, float)])

    # we want to return a number
    # we want to sum all the numbers in the list that are floats

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
