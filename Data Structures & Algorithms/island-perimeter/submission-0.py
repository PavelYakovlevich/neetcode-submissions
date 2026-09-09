class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                perimeter += self.calculate_perimeter(grid, r, c)
        
        return perimeter
    
    def calculate_perimeter(self, grid: List[List[int]], r: int, c: int) -> int:
        if not grid[r][c]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])

        cell_perimeter = 0
        for r_adj, c_adj in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            new_r, new_c = r + r_adj, c + c_adj
            if (min(new_r, new_c) < 0 or 
                new_r >= ROWS or 
                new_c >= COLS or 
                not grid[new_r][new_c]):
                cell_perimeter += 1
        return cell_perimeter