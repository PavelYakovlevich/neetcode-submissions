class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        heap = [[0, 0, 0]]
        visited = set()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while True:
            effort, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return effort
            
            for r_dir, c_dir in directions:
                r_new, c_new = r + r_dir, c + c_dir
                if (min(r_new, c_new) >= 0 and
                    r_new < ROWS and
                    c_new < COLS and
                    (r_new, c_new) not in visited
                ):
                    new_effort = abs(heights[r][c] - heights[r_new][c_new])
                    heapq.heappush(heap, [max(effort, new_effort), r_new, c_new])
