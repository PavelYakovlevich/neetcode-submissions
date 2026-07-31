class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i: int, j: int):
            if (min(i, j) < 0 or i == n or j == m or grid[i][j] == '0'):
                return
            
            grid[i][j] = '0'
            dfs(i, j - 1)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i + 1, j)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j) 
        
        return res


    
