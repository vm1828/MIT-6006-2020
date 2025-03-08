def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''

    count, largest_length = 0, 1

    i = 0
    while i < len(A):
        subarray_length = 1
        for j in range(i, len(A)-1):
            if A[j] >= A[j+1]:
                break
            subarray_length += 1

        if subarray_length == largest_length:
            count += 1
        elif subarray_length > largest_length:
            largest_length = subarray_length
            count = 1
        i += subarray_length

    return count
