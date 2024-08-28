def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # phrase is a string
    # to_swap is a string
    # we want to return a string
    # we want to return a string where each instance of to_swap in phrase is swapped
    # we want to return a string where the case of to_swap is swapped
    to_swap = to_swap.lower()
    swapped = ''
    
    for letter in phrase:
        if letter.lower() == to_swap:
            letter = letter.swapcase()
        swapped += letter
        
    return swapped

# $ python -m doctest -v flip_case.py
# 1 items had no tests:



