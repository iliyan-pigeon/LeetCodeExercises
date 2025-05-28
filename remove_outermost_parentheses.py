class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        mapping = {}
        score = 0

        if s == "":
            return ""

        for i, v in enumerate(s):
            mapping[i] = score

            if v == "(":
                score += 1
            elif v == ")":
                score -= 1

        first, second = sorted(set([i for i in mapping.values()]))[:2]
        result = ""

        for i in range(len(s)):
            if mapping[i] == first and s[i] == "(":
                continue
            elif mapping[i] == second and s[i] == ")":
                continue

            result += s[i]

        return result