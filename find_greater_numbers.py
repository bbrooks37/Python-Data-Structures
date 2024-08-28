def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    # nums is a list of numbers
    # we want to return a number
    # we want to return the number of times a number is followed by a greater number
    # we want to return 0 if there are no numbers in the list
    count = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                count += 1
                
    return count
    # When we run the doctests, we get this:
    # $ python3 -m doctest find_greater_numbers.py