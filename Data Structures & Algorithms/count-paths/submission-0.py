class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * m
        for r in range(n - 1, -1, -1):
            curr = [0] * m
            curr[-1] = 1

            for c in range(m - 2, -1, -1):
                curr[c] = curr[c + 1] + prev[c]
            
            prev = curr


        return curr[0]

