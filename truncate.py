def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    # phrase is a string
    # n is an integer
    # we want to return a string
    # if phrase is longer than n, return truncated version of phrase
    # if phrase is not longer than n, return phrase
    # if n is less than 3, return a message
    # if n is 3, return '...'
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    
    if n >= len(phrase):
        return phrase
    
    return phrase[:n - 3] + '...'
    # When we run the doctests, we get this:
    # $ python3 -m doctest truncate.py