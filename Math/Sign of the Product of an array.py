class Solution:
    def arraySign(self, nums: List[int]) -> int:
        Z = 0
        N = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                N += 1 
        if N % 2 == 0:
            return 1
        else:
            return -1
