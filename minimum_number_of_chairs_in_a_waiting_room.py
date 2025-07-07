class Solution:
    def minimumChairs(self, s: str) -> int:
        max_chairs = 0
        chairs_needed = 0

        for op in s:
            if op == "E":
                chairs_needed += 1

            elif op == "L":
                chairs_needed -= 1

            if chairs_needed > max_chairs:
                max_chairs = chairs_needed

        return max_chairs
