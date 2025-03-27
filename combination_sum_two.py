from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def add_unique(start, current_result, remaining_target):
            if remaining_target == 0:
                result.append(current_result[:])
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                number = candidates[i]
                if number <= remaining_target:
                    current_result.append(number)
                    add_unique(i + 1, current_result, remaining_target - number)
                    current_result.pop()

        add_unique(0, [], target)
        return result
      
