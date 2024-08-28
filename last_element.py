def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # we want to return the last element in the list
    # we want to return None if the list is empty
    if lst:
        return lst[-1]
    
    
    # we don't need to check if lst is empty because if lst is empty, the function will return None