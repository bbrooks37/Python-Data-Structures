def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    # if collection is a dictionary, we want to check if sought is in the values of the dictionary
    # if collection is a set, we want to check if sought is in the set
    # if start is None or collection is a set, we want to check if sought is in the collection
    # if collection is a string/list/tuple and start is provided, we want to start searching at that index
    if isinstance(collection, dict):
        return sought in collection.values()
    
    if start is None or isinstance(collection, set):
        return sought in collection
    
    return sought in collection[start:]

    # $ python -m doctest -v includes.py
    # 1 items had no tests: