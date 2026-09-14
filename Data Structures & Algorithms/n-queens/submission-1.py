class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        forbidden_cols, forbidden_pos_diags, forbidden_neg_diags = set(), set(), set()
        board = [(['.'] * n) for i in range(n)]

        def lock_cells(r, c):
            board[r][c] = 'Q'
            forbidden_cols.add(c)
            forbidden_pos_diags.add(r + c)
            forbidden_neg_diags.add(r - c)
        
        def unlock_cells(r, c):
            forbidden_cols.remove(c)
            forbidden_pos_diags.remove(r + c)
            forbidden_neg_diags.remove(r - c)
            board[r][c] = '.'

        def solve(r, queens_count):
            if r == n:
                res.append([''.join(board[i]) for i in range(n)])
                return
            
            for i in range(n):
                if (i not in forbidden_cols and
                    (r + i) not in forbidden_pos_diags and
                    (r - i) not in forbidden_neg_diags):
                    lock_cells(r, i)
                    solve(r + 1, queens_count + 1)
                    unlock_cells(r, i)

        solve(0, 0)
        
        return res