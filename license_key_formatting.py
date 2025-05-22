class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []
        s = reversed([i.upper() if i.isalpha() else i for i in s.replace("-", "")])

        current = []
        for i in s:
            current.insert(0, i)

            if len(current) == k:
                result.insert(0, "".join(current))
                current = []

        return "-".join(result)
      
