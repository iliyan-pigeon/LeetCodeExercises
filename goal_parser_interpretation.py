class Solution:
    def interpret(self, command: str) -> str:

        result = ""
        current = ""

        for ch in command:
            if ch == "G":
                result += "G"
            else:
                current += ch

                if current == "()":
                    result += "o"
                    current = ""
                elif current == "(al)":
                    result += "al"
                    current = ""

        return result
