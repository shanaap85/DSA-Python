class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = len(nums) - 1
        while a <= b:
            if nums[a] == val:
                if nums[b] != val:
                    nums[a], nums[b] = nums[b], nums[a]
                    a += 1
                    b -= 1
                else:
                    b -= 1
            else:
                a += 1
        return b+1
        
