class Solution(object):
    def maxArea(self, height):
        result = 0

        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                current = min(height[i], height[j]) * len(height[i:j])
                if current > result:
                    result = current

        return result
