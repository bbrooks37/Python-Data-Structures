def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # parens is a string
    # we want to return a boolean
    # we want to return True if the parentheses are validly balanced
    # we want to return False if the parentheses are not validly balanced
    count = 0
    
    for p in parens:
        if p == "(":
            count += 1
        elif p == ")":
            count -= 1
        if count < 0:
            return False
        
    return count == 0
    # Time complexity: O(n)
    # Space complexity: O(1)
    # where n is the length of parens
    