class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        pq = [[grid[0][0], 0, 0]]
        visit = {(0, 0)}

        while pq:
            level, r, c = heapq.heappop(pq)
            if r == c == n - 1:
                return level

            for r_dir, c_dir in directions:
                r_new, c_new = r + r_dir, c + c_dir
                if (
                    min(r_new, c_new) >= 0 and
                    max(r_new, c_new) < n and
                    (r_new, c_new) not in visit
                ):
                    visit.add((r_new, c_new))
                    heapq.heappush(pq, [max(level, grid[r_new][c_new]), r_new, c_new])