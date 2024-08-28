def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # phrase is a string
    # we want to return a boolean
    # we want to return True if phrase is a palindrome
    # we want to return False if phrase is not a palindrome
    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]
    
