def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    # nums is a list of numbers
    # we want to return a number
    # we want to return the product of the even numbers
    # we want to return 1 if there are no even numbers
    
    product = 1
    
    for num in nums:
        if num % 2 == 0:
            product *= num
            
    return product
    # When we run the doctests, we get this:
    # $ python3 -m doctest multiply_even_numbers.py