class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        curr_word = []
        ROWS, COLS = len(board), len(board[0])
        def search_word(r, c):
            if len(curr_word) > len(word):
                return False

            if len(curr_word) == len(word) and curr_word[-1] == word[-1]:
                return True

            res = False
            for r_adj, c_adj in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                new_r, new_c = r + r_adj, c + c_adj
                if (min(new_r, new_c) >= 0 and
                    new_r < ROWS and
                    new_c < COLS and
                    (new_r, new_c) not in visited and
                    board[new_r][new_c] == word[len(curr_word)]):
                    visited.add((new_r, new_c))
                    curr_word.append(board[new_r][new_c])
                    res = res or search_word(new_r, new_c)
                    visited.remove((new_r, new_c))
                    curr_word.pop()

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visited.add((r, c))
                    curr_word.append(board[r][c])
                    if search_word(r, c):
                        return True
                    visited.remove((r, c))
                    curr_word.pop()
        return False