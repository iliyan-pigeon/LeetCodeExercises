class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""

        current = ""

        for ch in address:
            if ch == ".":
                result += f"{current}[.]"
                current = ""
                continue

            current += ch

        result += current

        return result
