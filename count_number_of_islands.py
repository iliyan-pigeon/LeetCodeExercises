def count_number_of_islands(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbours(coord):
        res = []
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))
        return res

    def dfs(coord):
        r, c = coord
        if grid[r][c] == 0:
            return
        grid[r][c] = 0
        for neighbor in get_neighbours(coord):
            nr, nc = neighbor
            if grid[nr][nc] == 1:
                dfs(neighbor)

    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 1:
                dfs((r, c))
                count += 1
    return count