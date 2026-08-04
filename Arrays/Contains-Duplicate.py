class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for i in range(len(nums)):
            map.add(nums[i])
        if len(nums) == len(map):
            return False
        return True
