def isPalindrome(string):
    # Write your code here.
    s = ""
    for i in string:
        s = i + s
    if s == string:
        return True

    return False
    pass
