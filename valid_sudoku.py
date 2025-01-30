def isValidSudoku(board):
    left = 0
    right = 3
    start_row = 0
    end_row = 3

    result = True

    for i in range(9):
        sub_box_numbers = []
        row_numbers = [n for n in board[i] if n.isnumeric()]
        column_numbers = [n for n in [board[m][i] for m in range(9)] if n.isnumeric()]

        for j in range(start_row, end_row):
            for ch in board[j][left:right]:
                if ch.isnumeric():
                    sub_box_numbers.append(ch)

        if len(set(row_numbers)) != len(row_numbers) or \
                len(set(column_numbers)) != len(column_numbers) or \
                len(set(sub_box_numbers)) != len(sub_box_numbers):
            result = False
            break

        if (i + 1) % 3 == 0 and i != 0:
            left = 0
            right = 3
            start_row += 3
            end_row += 3
        else:
            left += 3
            right += 3

    return result
