# Solution 1
class Solution:
    def makeFancyString(self, s: str) -> str:
        left = 0
        right = 3
        while right <= len(s):
            substring = s[left:right]
            a = len(set(substring))
            if a == 1:
                s = s[:right-1]+s[right:]
            else:
                left += 1
                right += 1

        return s


# Solution 2
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""

        for ch in s:
            if len(result) > 1 and ch == result[-1] == result[-2]:
                continue

            result += ch
            
        return result
