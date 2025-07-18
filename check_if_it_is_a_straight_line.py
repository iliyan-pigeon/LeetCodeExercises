from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Calculate the initial slope using the first two points
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        # Handle vertical line case
        if x1 - x0 == 0:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != x0:
                    return False
            return True
        
        # Calculate the initial slope
        initial_slope = (y1 - y0) / (x1 - x0)
        
        # Check if all other points have the same slope
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if x - x0 == 0:
                return False  # Vertical line check
            slope = (y - y0) / (x - x0)
            if slope != initial_slope:
                return False
        
        return True
