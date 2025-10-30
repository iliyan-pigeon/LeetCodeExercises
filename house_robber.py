from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for house in nums:
            temp = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


a = Solution()
print(a.rob([8,9,9,4,10,5,6,9,7,9]))


# Failed hard thinking solution/not solution ;(
class Solution:
    def rob(self, nums: List[int]) -> int:
        ordered_nums = sorted([i for i in enumerate(nums)], key=lambda x: x[1], reverse=True)
        total_sum = 0
        all_total_sums = []
        robbed_indexes = []
        counter = 0

        while counter != len(ordered_nums):

            for i, num in ordered_nums:
                if not robbed_indexes:
                    robbed_indexes.append(i)
                    total_sum += num
                    continue

                adjacent = False

                for j in robbed_indexes:
                    if abs(j - i) in (0, 1):
                        adjacent = True
                        break

                if not adjacent:
                    total_sum += num
                    robbed_indexes.append(i)

            all_total_sums.append(total_sum)
            total_sum = 0
            robbed_indexes = []
            move_it = ordered_nums.pop(0)
            ordered_nums.append(move_it)
            counter += 1

        return max(all_total_sums)
