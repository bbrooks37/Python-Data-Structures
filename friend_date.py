def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    # a and b are tuples
    # we want to return a boolean
    # we want to return True if a and b have any hobbies in common
    # we want to return False if a and b do not have any hobbies in common
    if set(a[2]) & set(b[2]):
        return True
    else:
        return False
    
    # ALTERNATIVE SOLUTION:
    # return bool(set(a[2]) & set(b[2]))