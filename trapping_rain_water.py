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
