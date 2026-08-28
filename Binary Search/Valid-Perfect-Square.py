class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = 1
        b = num
        while a <= b:
            mid = (a + b)//2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                b = mid - 1
            elif mid ** 2 < num:
                a = mid + 1
        return False
