def sortedSquaredArray(array):
    # Write your code here.
    for i in range(0, len(array)):
        array[i] = array[i]*array[i]
    array.sort()
    return array
