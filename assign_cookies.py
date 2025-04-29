from typing import List


# Solution 1
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child = 0
        cookie = 0
        result = 0

        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:

                result += 1
                child += 1

            cookie += 1

        return result


# Solution 2
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort()
        s.sort()

        for i in g:
            for j in s:
                if i <= j:
                    result += 1
                    s.remove(j)
                    break

        return result
