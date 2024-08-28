def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    # nums is a list of numbers
    # we want to return a boolean
    # we want to return True if the sum of any 3 sequential numbers is odd
    # we want to return False if the sum of any 3 sequential numbers is even
    for i in range(len(nums) - 2):
        if sum(nums[i:i+3]) % 2 != 0:
            return True
        
    return False
    # When we run the doctests, we get this:
    # $ python3 -m doctest three_odd_numbers.py
