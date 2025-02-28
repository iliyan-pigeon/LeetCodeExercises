class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        for candy in candies:
            current = True
            for i in candies:
                if candy + extraCandies < i:
                    current = False
                    break

            result.append(current)

        return result
