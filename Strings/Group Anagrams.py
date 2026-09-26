class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        Map = {}
        for i in strs:
            if ''.join(sorted(i)) not in Map:
                Map[''.join(sorted(i))] = [i]
            else:
                Map[''.join(sorted(i))].append(i)
        L = []
        for i in Map:
            L.append(Map[i])

        return L
