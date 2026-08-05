class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values_frequencies = defaultdict(int)

        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                values_frequencies[grid[i][j]] += 1
        
        res = [0, 0]
        for i in range(1, (n ** 2) + 1):
            if values_frequencies[i] == 2:
                res[0] = i
            
            if not values_frequencies[i]:
                res[1] = i
        
        return res