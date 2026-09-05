class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        minimum = [0]*len(nums)
        maximum = [0]*len(nums)
        miN = float('inf')
        maX = float('-inf')
        for i in range(len(nums)):
            maX = max(nums[i], maX)
            maximum[i] = maX

        for j in range(len(nums) - 1, -1, -1):
            miN = min(nums[j], miN)
            minimum[j] = miN

        print(minimum)

        for i in range(len(nums)):
            if maximum[i] - minimum[i] <= k:
                return i

        return -1
