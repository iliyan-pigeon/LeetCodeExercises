class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        first = 0
        second = k

        result = len(blocks)

        while second <= len(blocks):
            current = blocks[first:second].count("W")

            if current < result:
                result = current

            first += 1
            second += 1

        return result
