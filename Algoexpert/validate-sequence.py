def isValidSubsequence(array, sequence):
    # Write your code here.
    index_arr = 0
    for i in array:
        if i == sequence[index_arr]:
            index_arr += 1
        if index_arr == len(sequence):
            return True
    return False

    pass
