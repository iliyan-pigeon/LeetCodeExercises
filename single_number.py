from typing import List


# Solution 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = {}

        for number in nums:
            if number not in nums_dict:
                nums_dict[number] = 0
            nums_dict[number] += 1

        result = [k for k, v in nums_dict.items() if v == 1][0]

        return result


  # Solution 2
  class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for number in nums:
            if nums.count(number) == 1:
                return number
      
