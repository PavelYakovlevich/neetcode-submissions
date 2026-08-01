class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        col_seen = defaultdict(set)
        row_seen = defaultdict(set)
        square_seen = defaultdict(set)

        for r in range(n):
            for c in range(n):
                char = board[r][c]

                if char == '.':
                    continue

                if (char in row_seen[r] 
                    or char in col_seen[c]
                    or char in square_seen[(r // 3, c // 3)]):
                    return False

                row_seen[r].add(char)
                col_seen[c].add(char)
                square_seen[((r // 3, c // 3))].add(char)
    
        return True