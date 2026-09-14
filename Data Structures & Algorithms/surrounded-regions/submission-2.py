class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def mark_area(r, c, replaceable_char, new_char):
            q = deque([[r, c]])
            board[r][c] = new_char
            while q:
                r, c = q.popleft()
                for r_adj, c_adj in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
                    new_r, new_c = r + r_adj, c + c_adj
                    if (min(new_r, new_c) >= 0 and 
                        new_r < ROWS and 
                        new_c < COLS and
                        board[new_r][new_c] == replaceable_char):
                        board[new_r][new_c] = new_char
                        q.append([new_r, new_c])

        for r in range(ROWS):
            for c in range(COLS):
                if (min(r, c) == 0 or r == ROWS - 1 or c == COLS - 1) and board[r][c] == 'O':
                    mark_area(r, c, 'O', 'B')
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    mark_area(r, c, 'O', 'X')

        for r in range(ROWS):
            for c in range(COLS):
                if (min(r, c) == 0 or r == ROWS - 1 or c == COLS - 1) and board[r][c] == 'B':
                    mark_area(r, c, 'B', 'O')