# Solution 1
class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


# Solution 2
class Solution(object):
    def trap(self, height):
        water = 0
        highest = 0

        for i, current_height in enumerate(height):
            if current_height >= highest and [h for index, h in enumerate(height[i:]) if index != 0 and h >=    current_height]:
                highest = current_height
            elif not [h for index, h in enumerate(height[i:]) if index != 0 and h >= current_height]:
                for h in sorted(height[i:], reverse=True):
                    if h < current_height:
                        highest = h
                        break
            elif current_height < highest and i < len(height) - 1:
                water += highest - current_height

        return water


# Solution 2.1
class Solution(object):
    def trap(self, height):
        water = 0
        highest = 0

        for i, current_height in enumerate(height):
            if current_height < highest and i < len(height) - 1:
                water += highest - current_height

            current_list = [h for index, h in enumerate(height[i:]) if index != 0 and h >= current_height]

            if current_height >= highest and current_list:
                highest = current_height
            elif not current_list:
                for h in sorted(height[i:], reverse=True):
                    if h < current_height:
                        highest = h
                        break

        return water
