# Solution 1
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        result = [i + 1 for i in range(len(nums)) if nums[i] > 0]

        return result


# Solution 2
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        for i in nums:
            result[i-1] = i

        return [i + 1 for i in range(len(result)) if result[i] == 0]


# Solution 3
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        set_nums = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                result.append(i)

        return result
