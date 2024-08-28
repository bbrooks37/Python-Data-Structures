def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    # a and b are numbers
    # operation is a string that is either 'add', 'subtract', 'multiply', or 'divide'
    # make_int is a boolean that defaults to False
    # message is a string that defaults to 'The result is'
    # we want to return a string that is the message followed by the result of the operation
    # we want to return None if the operation is not valid
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':\
        result = a / b
    else:
        return None
    
    if make_int:
        result = int(result)
        
    return f"{message} {result}"
    # When we run the doctests, we get this:
    # $ python3 -m doctest calculate.py
