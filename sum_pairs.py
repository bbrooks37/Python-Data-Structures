def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # nums is a list of numbers
    # goal is a number
    # we want to return a tuple of the first pair of numbers that sum to goal
    # we want to return an empty tuple if there are no pairs that sum to goal
    already_visited = set()
    
    for num in nums:
        target = goal - num
        
        if target in already_visited:
            return (target, num)
        
        already_visited.add(num)
        
    return ()

    # When we run the doctests, we get this:
    # $ python3 -m doctest sum_pairs.py
