class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a = 1
        b = 2
        sum = 0
        for i in range(3, n+1):
            sum = a + b
            a = b
            b = sum
        return sum        
