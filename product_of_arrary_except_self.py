# Solution 1
class Solution(object):
    def productExceptSelf(self, nums):
        answer = []

        for i in range(len(nums)):
            current_nums = [value for index, value in enumerate(nums) if index != i]
            result = 1
            for j in current_nums:
                result *= j
            answer.append(result)

        return answer


# Solution 2
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
