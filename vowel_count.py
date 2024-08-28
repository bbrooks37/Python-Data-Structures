def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # return {ltr: frequency} from phrase
    # phrase is a string
    # we want to return a dictionary
    # we want to return a dictionary where the keys are the vowels in phrase
    # we want to return a dictionary where the values are the frequency of the vowels in phrase
    phrase = phrase.lower()
    counter = {}
    
    for ltr in phrase:
        if ltr in 'aeiou':
            counter[ltr] = counter.get(ltr, 0) + 1
            
    return counter
    
    if __name__ == "__main__":
        return doctest.testmod()
    
    # python3 -m doctest -v vowel_count.py