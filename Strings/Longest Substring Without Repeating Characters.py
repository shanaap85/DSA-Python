class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        st = ''
        maxLength = 0
        for i in range(len(s)):
            if s[i] not in st:
                st += s[i]
            else:
                a = s.find(s[i], a, a + len(st))
                a += 1
                st = s[a: i+1]
            maxLength = max(len(st), maxLength)
        return maxLength
