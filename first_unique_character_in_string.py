# Solution 1
class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i, ch in enumerate(s):
            if s.count(ch) == 1:
                return i

        return -1


# Solution 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for i, ch in enumerate(s):
            if ch not in count:
                count[ch] = [i, 0]
            count[ch][1] += 1

        for c in count:
            if count[c][1] == 1:
                return count[c][0]

        return -1
        
