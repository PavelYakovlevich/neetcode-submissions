class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cells = deque()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    cells.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        time = -1
        while cells:
            for i in range(len(cells)):
                r, c = cells.popleft()
                for r_adj, c_adj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                    next_r, next_c = r + r_adj, c + c_adj
                    if (
                        min(next_r, next_c) >= 0 and
                        next_r < ROWS and
                        next_c < COLS and
                        grid[next_r][next_c] == 1
                    ):
                        grid[next_r][next_c] = 2
                        fresh -= 1
                        cells.append((next_r, next_c))

            time += 1
        
        return time if fresh == 0 else -1