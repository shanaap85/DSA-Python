"""
Problem: Two Sum
Difficulty: Easy
Concept: Hash Map

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


print(two_sum([2, 7, 11, 15], 9))

Add Two Sum solution : [0, 1]
