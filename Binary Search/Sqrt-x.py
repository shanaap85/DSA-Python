class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i*i <= x:
            if i*i == x:
                return i 
            elif i*i < x and (i+1)*(i+1) > x:
                return i
            i += 1
