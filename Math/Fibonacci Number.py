class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        a, b = 0, 1
        sum = 0
        for i in range(2,n+1):
            sum = a + b
            a = b
            b = sum
        return sum
