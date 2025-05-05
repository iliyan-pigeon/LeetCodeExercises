from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def change_colour(r, c, cl):
            if image[r][c] == cl:
                image[r][c] = color

        color_for_change = image[sr][sc]
        pixels_for_change = [[sr, sc]]
        already_processed = []

        while pixels_for_change:
            p = pixels_for_change[0]
            row = p[0]
            column = p[1]

            change_colour(row, column, color_for_change)
            pixels_for_change.pop(0)

            if row + 1 < len(image):
                if image[row+1][column] == color_for_change and [row+1, column] not in already_processed:
                    pixels_for_change.append([row+1, column])
                    already_processed.append([row+1, column])

            if row - 1 >= 0:
                if image[row - 1][column] == color_for_change and [row - 1, column] not in already_processed:
                    pixels_for_change.append([row - 1, column])
                    already_processed.append([row - 1, column])

            if column + 1 < len(image[row]):
                if image[row][column + 1] == color_for_change and [row, column + 1] not in already_processed:
                    pixels_for_change.append([row, column + 1])
                    already_processed.append([row, column + 1])

            if column - 1 >= 0:
                if image[row][column - 1] == color_for_change and [row, column - 1] not in already_processed:
                    pixels_for_change.append([row, column - 1])
                    already_processed.append([row, column - 1])

        return image
        
