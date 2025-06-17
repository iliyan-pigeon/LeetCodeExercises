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
