from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current_result = []

        def add_unique(start, current_result, remaining_target):
            if remaining_target == 0:
                result.append(current_result[:])  # Append a copy of the valid combination
                return

            for i in range(start, len(candidates)):
                number = candidates[i]
                if number <= remaining_target:
                    current_result.append(number)
                    add_unique(i, current_result, remaining_target - number)  # Recurse with the reduced target
                    current_result.pop()  # Backtrack to explore other possibilities

        add_unique(0, current_result, target)
        return result


# Unsuccessful attempt
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current_result = []

        def add_unique(candidates, current_result):
            for number in candidates:

                sum_current_result = sum(current_result)

                if number <= target - sum_current_result:
                    for _ in range((target - sum_current_result) // number):
                        current_result.append(number)

                    sum_current_result = sum(current_result)

                    if sum_current_result == target:
                        result.append(current_result)
                        current_result = []
                    else:
                        candidates_left = [i for i in candidates if (target - sum_current_result) >= i]

                        if not candidates_left:
                            return
                        else:
                            add_unique(candidates_left, current_result)
                            current_result = []

        add_unique(candidates, current_result)

        return result
