class Solution:
    def isHappy(self, n: int) -> bool:
        S = set()
        
        while n != 1:
            if n in S:
                return False
            
            S.add(n)

            Total = 0
            while n > 0:
                Total += (n%10) ** 2
                n //= 10

            n = Total
        
        return True
