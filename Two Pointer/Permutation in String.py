class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        Map1 = {}
        for i in s1:
            if i not in Map1 :
                Map1[i] = 1
            else:
                Map1[i] += 1

        for i in range(len(s2)):
            Map2 = {}
            for j in s2[i:len(s1)+i]:
                if j not in Map2:
                    Map2[j] = 1
                else:
                    Map2[j] += 1
            if Map1 == Map2:
                return True
        return False
