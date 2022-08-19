def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in array:
        diff = targetSum - i
        if diff in array and diff != i:
            return [diff, i]
    return []
    pass
