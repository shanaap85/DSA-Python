class Solution:
    def firstUniqChar(self, s: str) -> int:
        
         result = len(s)

         for i in 'abcdefghijklmnopqrstuvwxyz' :
            firstOccurance = s.find(i)

            if firstOccurance != -1 and firstOccurance == s.rfind(i) :
                if firstOccurance < result :
                    result = firstOccurance
                    
         return result if result != len(s) else -1
