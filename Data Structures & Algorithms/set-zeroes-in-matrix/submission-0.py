class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        copy = [row.copy() for row in matrix]

        M, N = len(matrix), len(matrix[0])

        for r in range(M):
            for c in range(N):
                if not copy[r][c]:
                    self.fill_col_row(matrix, r, c)

    def fill_col_row(self, matrix, r, c):
        for i in range(len(matrix)):
            matrix[i][c] = 0
        
        for i in range(len(matrix[r])):
            matrix[r][i] = 0