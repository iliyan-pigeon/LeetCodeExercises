# Solution
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        encrypted_string = ""

        for i in range(len(s)):
            index = i + k

            while index > len(s) - 1:
                index -= len(s)

            encrypted_string += s[index]

        return encrypted_string


# Solution 2
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        result = ""
        for i in range(len(s)):
            result += s[(i + k) % len(s)]
        return result
