from typing import List


class Solution:
    def findPositionedDuration(self, timeSeries: List[int], duration: int) -> int:
        seconds_poisoned = 0

        for i in range(len(timeSeries)):
            seconds_poisoned += duration
            if i+1 < len(timeSeries):
                if timeSeries[i] + duration >= timeSeries[i+1]:
                    seconds_poisoned -= (timeSeries[i] + duration) - timeSeries[i+1]

        return seconds_poisoned
      
