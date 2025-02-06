# Solution 1
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                    return True
            index_map[num] = i

        return False


# Solution 2
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        result = False

        if len(nums) == 2 and k >= 1 and nums[0] == nums[1]:
            return True

        for i in range(len(nums)):
            if i + k + 1 >= len(nums) + 1:
                if nums[i + 1:k + i].count(nums[i]) >= 2:
                    return True

            if nums[i] in nums[i + 1:k + i + 1]:
                result = True
                break

        return result


# Solution 3
def containsNearbyDuplicate(nums, k):
    result = False

    for i in range(len(nums)):
        for j in range(k, 0, -1):
            if i + j >= len(nums):
                continue
            if nums[i] == nums[i+j]:
                result = True
                break
        if result is True:
            break

    return result



# Solution 4
def containsNearbyDuplicate(nums, k):
    result = False

    for i in range(len(nums)):
        for j in range(k+1):
            if j + i == len(nums):
                break

            if nums[i] == nums[i+j] and i != i+j:
                result = True
                break

    return result
