class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res, n = 0, len(mat) 

        for i in range(n):
            res += mat[i][i] + (mat[i][n - i - 1] if i != n - i - 1 else 0)

        return res