from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s='', opened=0, closed=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if opened < n:
                backtrack(s + '(', opened + 1, closed)
            if closed < opened:
                backtrack(s + ')', opened, closed + 1)

        result = []
        backtrack()
        return result
