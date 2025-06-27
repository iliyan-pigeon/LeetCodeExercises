class Solution:
    def maximumLengthSutstring(self, s: str) -> int:
        left = 0
        right = 1

        result = 0

        while left < len(s):
            current = s[left:right]

            if len(set(current)) == len(current) or len(set(current)) + 1 == len(current):
                right += 1
                if len(current) > result:
                    result = len(current)
            else:
                left += 1

            if right >= len(s)+1:
                left += 1

        return result
