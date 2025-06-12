from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keyPressed: str) -> str:
        current_time = 0
        result_time = 0
        result = ""

        for i, time in enumerate(releaseTimes):
            current = time - current_time
            current_time = time

            if current > result_time:
                result_time = current
                result = keyPressed[i]

            elif current == result_time and result < keyPressed[i]:
                result_time = current
                result = keyPressed[i]

        return result
