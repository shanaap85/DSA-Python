"""
Problem: Maximum Subarray

Difficulty: Medium
Algorithm: Kadane's Algorithm

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode #53
"""


def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Maximum Subarray Sum:", max_subarray(nums))

[4, -1, 2, 1]
