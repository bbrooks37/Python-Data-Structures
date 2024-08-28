def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # nums is a list of numbers
    # we want to return a number
    # we want to return the duplicate number in nums
    # if there is no duplicate, we want to return None
    seen = set()
    
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
        
    return None
    # When we run the doctests, we get this:
    # $ python3 -m doctest find_the_duplicate.py
