from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count_elders = 0

        for person in details:
            if int(person[-4:-2]) > 60:
                count_elders += 1

        return count_elders
