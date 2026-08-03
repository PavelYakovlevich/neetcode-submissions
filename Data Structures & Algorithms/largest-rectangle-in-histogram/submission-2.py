class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start_index = i

            while stack and stack[-1][1] > h:
                pos, height = stack.pop()
                width = i - pos
                max_area = max(max_area, height * width)
                start_index = pos

            stack.append((start_index, h))

        for pos, h in stack:
            max_area = max(max_area, h * (len(heights) - pos))

        
        return max_area