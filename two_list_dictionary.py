def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    # keys is a list of keys
    # values is a list of values
    # we want to return a dictionary of keys and values
    # if there are fewer values than keys, the remaining keys should have a value of None
    # if there are fewer keys, we should ignore the remaining values
    out = {}
   
    for idx, key in enumerate(keys):
       out[key] = values[idx] if idx < len(values) else None
       
    return out
    # we can also use zip to combine two lists and then convert it to a dictionary
    # return dict(zip(keys, values))
    # $ python -m doctest -v two_list_dictionary.py
    # 1 items passed all tests: