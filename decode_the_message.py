class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        current_letter = 97

        decoder = {}
        result = ""

        for ch in key:
            if ch == " ":
                continue
            elif ch not in decoder:
                decoder[ch] = chr(current_letter)
                current_letter += 1

        for ch in message:
            if ch == " ":
                result += ch
            else:
                result += decoder[ch]

        return result
