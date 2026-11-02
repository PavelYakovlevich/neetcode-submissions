class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        
        q = deque([[0, 0, 1]])
        directions = [[1, 1], [1, 0], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
        visit = set([(0, 0)])

        while q:
            r, c, path = q.popleft()

            if r == c == N - 1:
                return path

            for r_dir, c_dir in directions:
                r_new, c_new = r + r_dir, c + c_dir
                
                if (min(r_new, c_new) < 0 or
                    max(r_new, c_new) >= N or
                    (r_new, c_new) in visit or
                    grid[r_new][c_new] == 1):
                    continue
                visit.add((r_new, c_new))
                q.append([r_new, c_new, path + 1])

        return -1