class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        heap = [[-grid[0][0], 0, 0]]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        seen = set([(0, 0)])
        score = float('inf')
        ROWS, COLS = len(grid), len(grid[0])
        while heap:
            cell_score, r, c = heapq.heappop(heap)
            score = min(score, -cell_score)
            if r == ROWS - 1 and c == COLS - 1:
                return score

            for r_adj, c_adj in directions:
                r_new, c_new = r + r_adj, c + c_adj
                if (min(r_new, c_new) < 0 or
                    r_new == ROWS or
                    c_new == COLS or
                    (r_new, c_new) in seen):
                    continue
                seen.add((r_new, c_new))
                heapq.heappush(heap, [-grid[r_new][c_new], r_new, c_new])
            