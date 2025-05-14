import sys
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(10001)
        return [int(i) for i in str(int("".join([str(i) for i in num])) + k)]
