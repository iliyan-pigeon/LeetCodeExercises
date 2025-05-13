from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        if arr[0] >= arr[1]:
            return False

        result = True
        direction = "Up"
        current_number = -float("inf")

        for number in arr:
            if direction == "Up":
                if number < current_number:
                    direction = "Down"
                elif number == current_number:
                    result = False
                    break

            elif direction == "Down":
                if number >= current_number:
                    result = False
                    break

            current_number = number

        if direction == "Up":
            result = False

        return result
        
