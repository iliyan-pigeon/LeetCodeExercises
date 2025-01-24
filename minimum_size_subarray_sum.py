import sys


# Solution 1
#def minSubArrayLen(target, nums):
#    counter = 1
#    minimal_subarray = sys.maxsize
#
#    while counter <= len(nums):
#
#        for i in range(len(nums)):
#            sum_numbers = sum(nums[i:i+counter])
#            if sum_numbers >= target:
#                minimal_subarray = counter
#                counter = len(nums)
#                break
#
#        counter += 1
#
#    if minimal_subarray != sys.maxsize:
#        return minimal_subarray
#
#    return 0


# Solution 2
def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    minimal_subarray = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window as long as the current sum is greater than or equal to the target
        while current_sum >= target:
            minimal_subarray = min(minimal_subarray, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return minimal_subarray if minimal_subarray != float('inf') else 0
