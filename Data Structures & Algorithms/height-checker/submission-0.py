class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()

        res = 0
        for i in range(len(heights)):
            res += int(heights[i] != expected[i])
        return res