class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        reverse = True
        for i in range(0, len(s), k):
            if reverse:
                result += s[i:i + k][::-1]
                reverse = False
            else:
                result += s[i:i + k]
                reverse = True

        return result
      
