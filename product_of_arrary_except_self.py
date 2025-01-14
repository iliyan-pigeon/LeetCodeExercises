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
