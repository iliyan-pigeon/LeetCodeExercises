# Solution one
class Solution(object):
    def twoSum(self, numbers, target):
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]


# Solution two
class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1  
