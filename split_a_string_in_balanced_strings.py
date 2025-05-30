class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        current = {"R": 0, "L": 0}

        for ch in s:
            current[ch] += 1

            if current["R"] == current["L"]:
                result += 1
                current["R"] = 0
                current["L"] = 0

        return result
