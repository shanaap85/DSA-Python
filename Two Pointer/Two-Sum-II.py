class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        freq = {}

        for i in range(n):
            comp = target - nums[i]

            if comp in freq:
                return [freq[comp], i]

            freq[nums[i]] = i
