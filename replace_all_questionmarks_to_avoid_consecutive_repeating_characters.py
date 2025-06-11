class Solution:
    def modifyString(self, s: str) -> str:
        character = 97

        for i, ch in enumerate(s):
            if ch == "?":
                while True:
                    if character == 123:
                        character = 97
                    if i-1 >= 0:
                        if ord(s[i-1]) == character:
                            character += 1
                            continue
                    if i+1 < len(s):
                        if ord(s[i+1]) == character:
                            character += 1
                            continue
                    break

                s = s.replace("?", chr(character), 1)

        return s
