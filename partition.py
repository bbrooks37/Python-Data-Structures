def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    # lst is a list of items
    # fn is a function that returns True or False
    # we want to return a list of lists
    # we want to return a list of 2 lists
    # the first list contains items that passed the fn test
    # the second list contains items that failed the fn test
    true_list = []
    false_list = []
    
    for item in lst:
        if fn(item):
            true_list.append(item)
        else:
            false_list.append(item)
            
    return [true_list, false_list]
    # When we run the doctests, we get this:
    # $ python3 -m doctest partition.py