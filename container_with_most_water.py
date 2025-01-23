# Solution 1
class Solution(object):
    def maxArea(self, height):
        result = 0

        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                current = min(height[i], height[j]) * len(height[i:j])
                if current > result:
                    result = current

        return result


# Solution 2
class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

