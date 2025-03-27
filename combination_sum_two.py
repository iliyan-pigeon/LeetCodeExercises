from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Step 1: Sort to handle duplicates

        def add_unique(start, current_result, remaining_target):
            if remaining_target == 0:
                result.append(current_result[:])  # Found a valid combination
                return

            for i in range(start, len(candidates)):
                # Step 3: Skip duplicate elements at the same depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                number = candidates[i]
                if number <= remaining_target:
                    current_result.append(number)
                    add_unique(i + 1, current_result, remaining_target - number)  # Move forward (i+1)
                    current_result.pop()  # Backtrack

        add_unique(0, [], target)
        return result
      
