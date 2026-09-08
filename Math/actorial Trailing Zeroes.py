class Solution:
    def trailingZeroes(self, n: int) -> int:
        j = 1
        count5 = 0
        while 5 ** j <= n:
            count5 += n//(5**j)
            j += 1
        return count5
