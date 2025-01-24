import sys


def minSubArrayLen(target, nums):
    counter = 1
    minimal_subarray = sys.maxsize

    while counter <= len(nums):

        for i in range(len(nums)):
            sum_numbers = sum(nums[i:i+counter])
            if sum_numbers >= target:
                minimal_subarray = counter
                counter = len(nums)
                break

        counter += 1

    if minimal_subarray != sys.maxsize:
        return minimal_subarray

    return 0
