class Solution:
    def countPoints(self, rings: str) -> int:
        the_rings = {}

        for i in range(1, len(rings), 2):
            if rings[i] not in the_rings:
                the_rings[rings[i]] = []
            the_rings[rings[i]].append(rings[i-1])

        return len([k for k, v in the_rings.items() if len(set(v)) == 3])
