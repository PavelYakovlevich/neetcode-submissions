class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def set_distances(r, c, distance):
            cells_q = deque([(r, c, 0)])

            while cells_q:
                curr_r, curr_c, curr_distance = cells_q.popleft()

                for r_adj, c_adj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    r, c = curr_r + r_adj, curr_c + c_adj

                    if (min(r, c) >= 0 and
                        r < ROWS and
                        c < COLS and
                        grid[r][c] != -1 and
                        grid[r][c] > curr_distance + 1):
                        grid[r][c] = curr_distance + 1
                        cells_q.append((r, c, curr_distance + 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c]:
                    set_distances(r, c, 0)