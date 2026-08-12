class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        A = s.strip().split(' ')
        return len(A[-1])
