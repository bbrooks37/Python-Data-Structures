def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # make a dictionary to hold the counts of each number
    counts = {}
    
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    # find the number with the highest count
    
    max_num = max(counts.values())
    
    # now we need to find the key that corresponds to that value
    
    for (num, count) in counts.items():
        if count == max_num:
            return num
    # we can also use a list comprehension to do this in one line
    # return [num for num, count in counts.items() if count == max_num][0]