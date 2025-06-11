class Solution:
    def modifyString(self, s: str) -> str:
        character = 97

        for i, ch in enumerate(s):
            if ch == "?":
                if i-1 >= 0:
                    if ord(s[i-1]) == character:
                        character += 1
                if i+1 < len(s):
                    if ord(s[i+1]) == character:
                        character += 1

                s = s.replace("?", chr(character))

        return s
