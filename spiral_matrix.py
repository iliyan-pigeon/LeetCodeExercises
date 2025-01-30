def spiralOrder(matrix):
    direction = "right"
    column = 0
    row = 0
    columns_amount = len(matrix(0))
    rows_amount = len(matrix)

    result = []
    matrix_symbols_length = sum(len(the_row) for the_row in matrix)

    while len(result) < matrix_symbols_length:
        current_number = matrix[row][column]
        result.append(current_number)

        if direction == "right":
            if column + 1 == columns_amount:
                row += 1
                direction = "down"
                continue
            elif matrix[row][column+1] in result:
                row += 1
                direction = "down"
                continue
            column += 1
        elif direction == "down":
            if row + 1 == rows_amount:
                column -= 1
                direction = "left"
                continue
            elif matrix[row + 1][column] in result:
                column -= 1
                direction = "left"
                continue
            row += 1
        elif direction == "left":
            if column == 0:
                row -= 1
                direction = "up"
                continue
            elif matrix[row][column-1] in result:
                row -= 1
                direction = "up"
                continue
            column -= 1
        elif direction == "up":
            if row == 0:
                column += 1
                direction = "right"
                continue
            elif matrix[row-1][column] in result:
                column += 1
                direction = "right"
                continue
            row -= 1

    return result

