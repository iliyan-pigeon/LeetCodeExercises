from collections import Counter
from functools import reduce
from math import gcd
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False

        cards_count = Counter(deck)
        counts = list(cards_count.values())

        gcd_values = reduce(gcd, counts)

        return gcd_values >= 2
