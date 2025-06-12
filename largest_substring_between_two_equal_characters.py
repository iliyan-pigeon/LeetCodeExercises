class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1

        positions = {}

        for i, ch in enumerate(s):
            if ch not in positions:
                positions[ch] = []
            positions[ch].append(i)

        for pos in positions.values():
            if len(pos) != 1:
                current = len(s[pos[0]:pos[-1]])-1

                if current > result:
                    result = current

        return result
