class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        res = [[0 for _ in range(n)] for _ in range(m)]
        for i, val in enumerate(original):
            r = i // n
            c = i % n
            res[r][c] = val
        return res
