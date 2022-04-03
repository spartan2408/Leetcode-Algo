class Solution:
    def solve(self, num):
        sum = 0
        while(num > 0):
            d = num % 10
            sum = sum+d
            num = num//10
        return sum
