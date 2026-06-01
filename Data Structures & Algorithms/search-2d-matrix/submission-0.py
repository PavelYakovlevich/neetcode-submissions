class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_count = len(matrix)
        cols_count = len(matrix[0])

        l = 0
        r = (rows_count * cols_count) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            mi = mid // cols_count
            mj = mid - (cols_count * mi)

            if matrix[mi][mj] == target:
                return True
            
            if target < matrix[mi][mj]:
                r = mid - 1
            else:
                l = mid + 1

        return False