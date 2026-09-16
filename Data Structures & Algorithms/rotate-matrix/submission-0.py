class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix) // 2):
                matrix[r][c], matrix[r][-1 - c] = matrix[r][-1 - c], matrix[r][c]
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix)): 
                matrix[len(matrix) - 1 - j][i], matrix[len(matrix) - 1 - i][j] = matrix[len(matrix) - 1 - i][j], matrix[len(matrix) - 1 - j][i]