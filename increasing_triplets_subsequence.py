from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    result = False

    for i in range(len(nums)-2):
        current_number = nums[i]

        for j in range(i+1, len(nums)-1):
            if nums[j] > current_number:
                current_number = nums[j]

                for k in range(j+1, len(nums)):
                    if nums[k] > current_number:
                        result = True
                        break
            if result is True:
                break
            current_number = nums[i]

        if result is True:
            break

    return result


print(increasingTriplet([1,5,0,4,1,3]))
