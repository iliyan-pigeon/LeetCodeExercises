# Solution 1
class Solution:
    def removeDuplicates(self, s: str) -> str:
        finished = False
        while not finished:
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    s = s[:i]+s[i+2:]
                    break
            else:
                finished = True

        return s


# Solution 2
class Solution:
    def removeDuplicates(self, s: str) -> str:
        index = 0
        
        while index < len(s)-1:
            if s[index] == s[index+1]:
                s = s[:index]+s[index+2:]
                index = max(0, index-1)
            else:
                index += 1

        return s
