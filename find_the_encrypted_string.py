class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        encrypted_string = ""

        for i in range(len(s)):
            index = i + k

            if index > len(s)-1:
                index -= len(s)

            encrypted_string += s[index]

        return encrypted_string
