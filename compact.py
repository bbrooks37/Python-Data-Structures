def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # lst is a list
    # we want to return a list
    # we want to return a list with all non-true elements
    return [val for val in lst if val]

    # $ python test_compact.py