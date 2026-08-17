class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

        return True

    def isPalindrome(self, s, a, b):
        while a < b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True
