class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        sub_length = 1
        result = 0

        while sub_length < len(s)+1:

            for i in range(len(s)+1-sub_length):
                current = s[i:i+sub_length]
                if current.count("0") <= k or current.count("1") <= k:
                    result += 1

            sub_length += 1

        return result