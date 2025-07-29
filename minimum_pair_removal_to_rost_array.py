class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0

        while nums != sorted(nums):
            min_pair = float("inf")
            start_index = None
            for i in range(len(nums)-1):
                current = nums[i] + nums[i+1]
                if current < min_pair:
                    min_pair = current
                    start_index = i

            new_nums = nums[:start_index]
            new_nums.append(min_pair)
            new_nums.extend(nums[start_index+2:])
            operations += 1

            nums = new_nums

        return operations
    