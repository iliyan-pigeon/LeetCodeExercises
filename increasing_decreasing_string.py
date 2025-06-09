class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        s = sorted(list(s))
        step = 1

        while s:
            if step == 1:
                result += s.pop(0)
                step += 1
            elif step == 2:
                counter = 0
                for i in range(len(s)):
                    if s[i-counter] > result[-1]:
                        result += s.pop(i-counter)
                        counter += 1
                step += 1
            elif step == 3:
                result += s.pop()
                step += 1
            elif step == 4:
                counter = 0
                for i in range(len(s)-1, -1, -1):
                    if s[i-counter] < result[-1]:
                        result += s.pop(i-counter)
                        counter += 1
                step = 1

        return result
