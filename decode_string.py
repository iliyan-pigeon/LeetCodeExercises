# Not completed 
class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        multiplier = 0
        current = ""
        next_index = 0

        for i, ch in enumerate(s):
            if i != next_index:
                continue
            if ch.isnumeric():
                current_multiplier = ch
                next_index = i + 1
                while s[next_index].isnumeric():
                    current_multiplier += s[next_index]
                    next_index += 1
                if not current:
                    multiplier = int(current_multiplier)
                else:
                    current += self.decodeString(s[i:])
                    next_index = i + len(s[i:]) - 2
            elif ch == "]":
                result += multiplier * current
                current = ""
                multiplier = 0
            elif ch != "[":
                if multiplier == 0:
                    result += ch
                else:
                    current += ch
            next_index += 1

        return result


a = Solution()
print(a.decodeString("100[leetcode]"))
