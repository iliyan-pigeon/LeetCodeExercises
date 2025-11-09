from typing import List


def subarray_sum_fixed(nums: List[int], k: int) -> int:
    max_sum = 0

    for i in range(len(nums)-k+1):
        current = sum(nums[i:i+k])
        if current > max_sum:
            max_sum = current

    return max_sum


print(subarray_sum_fixed([1, 5, 2, 7, 6], 2))
