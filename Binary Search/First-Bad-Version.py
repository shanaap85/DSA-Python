class Solution:
    def firstBadVersion(self, n: int) -> int:
        a = 0
        b = n
        mid = (a+ b)//2

        while a < b:
            mid = (a + b)//2
            if isBadVersion(mid) == True:
                b = mid
            else:
                a = mid + 1
        return a
