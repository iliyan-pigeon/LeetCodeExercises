class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_position = points[0][1]

        for start, end in points:
            if start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows
    