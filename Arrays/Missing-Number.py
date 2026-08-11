class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        xorL = nums[0]
        for i in range(1, len(nums)):
            xorL = xorL ^ nums[i]
            xor = xor ^ (i)
        xor = xor ^ len(nums)
        return xor ^ xorL
