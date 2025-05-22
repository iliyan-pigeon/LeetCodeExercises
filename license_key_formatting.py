# Solution 1
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []
        s = reversed(s.replace('-', '').upper())

        current = []
        for i in s:
            current.insert(0, i)

            if len(current) == k:
                result.insert(0, "".join(current))
                current = []

        if current:
            result.insert(0, "".join(current))

        return "-".join(result)


# Solution 2
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        n = len(s)

        first_group = n % k or k
        res = [s[:first_group]]

        for i in range(first_group, n, k):
            res.append(s[i:i + k])
            
        return '-'.join(res)
