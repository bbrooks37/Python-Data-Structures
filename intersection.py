def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # l1 and l2 are lists
    # we want to return a list
    # we want to return the intersection of l1 and l2
    # we want to return an empty list if there is no intersection
    set1 = set(l1)
    set2 = set(l2)
    
    return list(set1 & set2)
    # When we run the doctests, we get this:
    # $ python3 -m doctest intersection.py