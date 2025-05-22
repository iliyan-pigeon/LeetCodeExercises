class Solution:
    def findLUSlength(self, a: str, b):
        if a == b:
            return -1
        
        return max(len(a), len(b))
      
