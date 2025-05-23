class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        result = 0

        left = 0
        right = 1

        while left < len(s) or right < len(s):
            current = s[left:right]

            count_zero = current.count("0")
            count_one = current.count("1")

            if count_zero >= 1 and count_one >= 1:
                substrings = min(count_one, count_zero)
                movement = max(count_one, count_zero)
                result += substrings
                left += movement
                right += movement
            else:
                if right >= len(s):
                    left += 1
                else:
                    right += 1

        return result
