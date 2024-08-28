def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    # d is a dictionary
    # we want to return a tuple of the minimum and maximum keys in the dictionary
    # we can use the min and max functions on the keys of the dictionary
    keys = d.keys()
    
    return (min(keys), max(keys))
    # we can also use the min and max functions directly on the dictionary
    # return (min(d), max(d))
    # $ python -m doctest -v min_max_key_in_dictionary.py
            