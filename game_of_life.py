class Solution(object):
    def gameOfLife(self, board):
        one_to_zero = []
        zero_to_one = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                current_number = board[i][j]
                neighbours = []

                if i == len(board) - 1 and i == 0:
                    if j == len(board[0]) - 1 and j == 0 and current_number == 1:
                        one_to_zero.append([i, j])
                    elif j == len(board[0]) - 1:
                        one_to_zero.append([i, j])
                    elif j == 0:
                        one_to_zero.append([i, j])
                    else:
                        neighbours.append(board[i][j+1])
                        neighbours.append(board[i][j-1])
                elif i == len(board) - 1:
                    if j == len(board[0]) - 1 and j == 0 and current_number == 1:
                        one_to_zero.append([i, j])
                    elif j == len(board[0]) - 1:
                        neighbours.append(board[i][j-1])
                        neighbours.append(board[i-1][j])
                        neighbours.append(board[i-1][j - 1])
                    elif j == 0:
                        neighbours.append(board[i][j+1])
                        neighbours.append(board[i-1][j])
                        neighbours.append(board[i-1][j+1])
                    else:
                        neighbours.append(board[i][j+1])
                        neighbours.append(board[i-1][j+1])
                        neighbours.append(board[i-1][j])
                        neighbours.append(board[i-1][j-1])
                        neighbours.append(board[i][j-1])
                elif i == 0:
                    if j == len(board[i]) - 1 and j == 0 and current_number == 1:
                        one_to_zero.append([i, j])
                    elif j == len(board[0]) - 1:
                        neighbours.append(board[i][j-1])
                        neighbours.append(board[i+1][j-1])
                        neighbours.append(board[i+1][j])
                    elif j == 0:
                        neighbours.append(board[i][j+1])
                        neighbours.append(board[i+1][j+1])
                        neighbours.append(board[i+1][j])
                    else:
                        neighbours.append(board[i][j+1])
                        neighbours.append(board[i+1][j+1])
                        neighbours.append(board[i+1][j])
                        neighbours.append(board[i+1][j-1])
                        neighbours.append(board[i][j-1])
                else:
                    if j == len(board[0]) - 1 and j == 0 and current_number == 1:
                        neighbours.append(board[i-1][j])
                        neighbours.append(board[i+1][j])
                    elif j == len(board[0]) - 1:
                        neighbours.append(board[i-1][j])
                        neighbours.append(board[i-1][j-1])
                        neighbours.append(board[i][j-1])
                        neighbours.append(board[i+1][j-1])
                        neighbours.append(board[i+1][j])
                    elif j == 0:
                        neighbours.append(board[i-1][j])
                        neighbours.append(board[i-1][j+1])
                        neighbours.append(board[i][j+1])
                        neighbours.append(board[i+1][j+1])
                        neighbours.append(board[i+1][j])
                    else:
                        neighbours.append(board[i][j+1])
                        neighbours.append(board[i+1][j+1])
                        neighbours.append(board[i+1][j])
                        neighbours.append(board[i+1][j-1])
                        neighbours.append(board[i][j-1])
                        neighbours.append(board[i-1][j-1])
                        neighbours.append(board[i-1][j])
                        neighbours.append(board[i-1][j+1])

                live_neighbours = neighbours.count(1)

                if current_number == 1:

                    if live_neighbours < 2 or live_neighbours > 3:
                        one_to_zero.append([i, j])
                elif current_number == 0:
                    if live_neighbours == 3:
                        zero_to_one.append([i, j])

        for location in one_to_zero:
            row = location[0]
            column = location[1]

            board[row][column] = 0

        for location in zero_to_one:
            row = location[0]
            column = location[1]

            board[row][column] = 1

        return board

