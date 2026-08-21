class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        Ans = ""
        for i in strs:
            if len(i) < len(s):
                s = i
        for j in range(len(s)):
            count = 0
            for h in strs:
                if h[j] == s[j]:
                    count += 1
                else: 
                    return Ans
            if count == len(strs):
                Ans += s[j]
        return Ans
