class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            current = ""
            group = 0

            for i in range(len(s)):
                if i % k == 0 and i != 0:
                    current += str(group)
                    group = int(s[i])
                else:
                    group += int(s[i])

            if group:
                current += str(group)

            s = current

        return s
