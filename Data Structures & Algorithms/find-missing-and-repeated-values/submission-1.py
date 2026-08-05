class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        frequencies = 0

        n = len(grid)
        res = [0, 0]
        for i in range(n):
            for j in range(n):
                mask = (1 << grid[i][j])
                frequencies ^= mask
                if not (frequencies & mask):
                    res[0] = grid[i][j]
        
        for i in range(1, n ** 2 + 1):
            mask = (1 << i)
            if not (frequencies & mask) and i != res[0]:
                res[1] = i
                break

        return res