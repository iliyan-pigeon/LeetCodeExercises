class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        result = 0

        left = 0
        right = 1

        while left != len(s)-1 and right != len(s)-1:
            current = s[left:right]

            count_zero = current.count("0")
            count_one = current.count("1")

            if count_zero == count_one:
                result += count_zero
                left += 1
            else:
                right += 1

        return result
