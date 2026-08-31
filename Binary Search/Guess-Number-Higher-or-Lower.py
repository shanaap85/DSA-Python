class Solution:
    def guessNumber(self, n: int) -> int:
        a = 0
        b = n
        while a <= b:
            mid = (a + b)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                b = mid -1
            elif guess(mid) == 1:
                a = mid + 1
