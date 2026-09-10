class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        curr_word = []
        ROWS, COLS = len(board), len(board[0])
        def search_word(r, c):
            if len(curr_word) == len(word) and curr_word[-1] == word[-1]:
                return True
                
            if (len(curr_word) > len(word) or 
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                (r, c) in visited or
                (curr_word and curr_word[-1] != word[len(curr_word) - 1])):
                return False

            visited.add((r, c))
            curr_word.append(board[r][c])

            res = False
            for r_adj, c_adj in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                res = res or search_word(r + r_adj, c + c_adj)

            visited.remove((r, c))
            curr_word.pop()

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if search_word(r, c):
                        return True
        return False