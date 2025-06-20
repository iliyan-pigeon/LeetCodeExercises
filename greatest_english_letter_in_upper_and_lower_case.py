class Solution:
    def greatestLetter(self, s: str) -> str:
        result = 64
        s = set(s)

        for ch in s:
            if ch.islower():
                if ch.upper() in s and ord(ch.upper()) > result:
                    result = ord(ch.upper())
            elif ch.isupper():
                if ch.lower() in s and ord(ch) > result:
                    result = ord(ch)

        if result == 64:
            return ""
        
        return chr(result)
