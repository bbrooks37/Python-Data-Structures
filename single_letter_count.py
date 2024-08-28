def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    # word is a string
    # letter is a string
    # we want to return a number
    # we want to return the number of times letter appears in word
    # we want to return 0 if letter does not appear in word
    return word.lower().count(letter.lower())