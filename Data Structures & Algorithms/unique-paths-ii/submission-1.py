class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = defaultdict(int)
        dp[(-1, 0)] = 1

        for r in range(0, ROWS):
            for c in range(0, COLS):
                if not obstacleGrid[r][c]:
                    dp[(r, c)] = dp[(r - 1, c)] + dp[(r, c - 1)]
        
        return dp[(ROWS - 1, COLS - 1)]
