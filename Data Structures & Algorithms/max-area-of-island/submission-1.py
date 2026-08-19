class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        offsets = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        M, N = len(grid), len(grid[0])
        seen = set()

        def dfs(R, C):
            if (min(R, C) < 0 or
                R == M or
                C == N or
                grid[R][C] == 0 or
                (R, C) in seen):
                return 0

            seen.add((R, C))

            surrounding_area = 0
            for r_offset, c_offset in offsets:
                surrounding_area += dfs(R + r_offset, C + c_offset)
            
            return 1 + surrounding_area

        res = 0
        for R in range(M):
            for C in range(N):
                if grid[R][C] == 1:
                    island_area = dfs(R, C)
                    res = max(res, island_area)
        
        return res
