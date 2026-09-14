class Solution:
        

    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def try_surround(i, j):
            seen = {(i, j)}
            q = deque([[i, j]])
            surrounded = True
            while q:
                r, c = q.popleft()
                if min(r, c) == 0 or r == ROWS - 1 or c == COLS - 1:
                    surrounded = False

                for r_adj, c_adj in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                    next_r, next_c = r + r_adj, c + c_adj
                    if (min(next_r, next_c) >= 0 and 
                        next_r < ROWS and 
                        next_c < COLS and 
                        board[next_r][next_c] == 'O' and 
                        (next_r, next_c) not in seen):
                            seen.add((next_r, next_c))
                            q.append([next_r, next_c])

            if surrounded:
                for r, c in seen:
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    try_surround(r, c)