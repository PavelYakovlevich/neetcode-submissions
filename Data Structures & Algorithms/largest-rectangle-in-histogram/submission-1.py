class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = heights[0]

        for i in range(n):
            if not heights[i]:
                continue
            
            local_min_height = heights[i]
            
            j = i
            while j < n and heights[j]:
                local_min_height = min(local_min_height, heights[j])
                local_area = ((j - i) + 1) * local_min_height
                max_area = max(max_area, local_area)

                j += 1

        return max_area