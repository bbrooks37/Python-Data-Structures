def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    # lst is a list
    # search_term is an integer
    # we want to return an integer
    # we want to return the frequency of search_term in lst
    return lst.count(search_term)