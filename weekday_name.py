def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # day_of_week is an integer
    # we want to return a string
    # we want to return the name of the weekday
    # we want to return None if the day_of_week is not between 1 and 7
    
    DAYS = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    
    if day_of_week < 1 or day_of_week > 7:
        return None
    
    return DAYS.get(day_of_week) 
    # When we run the doctests, we get this:
    # $ python3 -m doctest weekday_name.py