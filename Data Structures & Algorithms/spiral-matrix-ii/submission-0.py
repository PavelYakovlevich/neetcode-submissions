class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        filled = 0
        i = j = 0
        di, dj = 0, 1
        while filled < n * n:
            matrix[i][j] = filled + 1
            filled += 1
            ni, nj = i + di, j + dj
            if not (0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 0):
                di, dj = dj, -di
                ni, nj = i + di, j + dj
            i, j = ni, nj

        return matrix