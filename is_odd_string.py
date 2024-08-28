def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
    # word is a string
    # we want to return a boolean
    # we want to return True if the sum of the character-positions is odd
    # we want to return False if the sum of the character-positions is even
    DIFF = ord('a') - 1
    
    total = sum(ord(char.lower()) - DIFF for char in word)
    
    return total % 2 == 1
    # When we run the doctests, we get this:
    # $ python3 -m doctest is_odd_string.py

    # Hint: you may find the ord() function useful here