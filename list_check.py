def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # we can use the all() function to check if all items in lst are lists
    for item in lst:
        if not isinstance(item, list):
            return False
        
    return True

    # we want to return a boolean
    # we want to check if all items in lst are lists
