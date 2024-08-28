def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
    
    with open(filename) as file:
        for line in file:
            print(f"- {line.strip()}")
            
    # filename is a string
    # we want to return None
    # we want to open the file and read each line
    # we want to print each line with a "-" before it
    # we want to strip off the newline character at the end of each line
    # we want to handle the case where the file cannot be found
    

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!