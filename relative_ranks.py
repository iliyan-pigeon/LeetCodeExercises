from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ordered_score = sorted(score, reverse=True)
        result = []

        for player in score:
            index = ordered_score.index(player)

            if index == 0:
                result.append("Gold Medal")
            elif index == 1:
                result.append("Silver Medal")
            elif index == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(index + 1))

        return result
      
