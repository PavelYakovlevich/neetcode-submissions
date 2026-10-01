class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rows_count = [0] * ROWS
        cols_count = [0] * COLS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rows_count[r] += 1
                    cols_count[c] += 1
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and max(rows_count[r], cols_count[c]) > 1:
                    res += 1
        return res