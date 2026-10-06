class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed) or name[0] != typed[0] or name[-1] != typed[-1]:
            return False 
        
        a = len(name) - 1
        b = len(typed) - 1

        while a >= 0 and b >= 0:
            if name[a] == typed[b]:
                a -= 1
                b -= 1
            elif typed[b] != typed[b+1]:
                return False
            else:
                b -= 1
        return True if a == -1 else False
