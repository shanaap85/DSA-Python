class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N0, N1, N2 = 0, 0, 0

        for i in nums:
            N0 += 1 if i == 0 else 0
            N1 += 1 if i == 1 else 0
            N2 += 1 if i == 2 else 0
        
        for i in range(len(nums)):
            if N0 != 0:
                nums[i] = 0
                N0 -= 1
            elif N1 != 0:
                nums[i] = 1
                N1 -= 1
            else:
                nums[i] = 2
