class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr_str = []
        res = []
        def backtracking(close_c, open_c):
            if close_c > open_c:
                return
                
            if len(curr_str) == 2 * n:
                if close_c == open_c:
                    res.append(''.join(curr_str))
                return
            
            curr_str.append('(')
            backtracking(close_c, open_c + 1)
            curr_str.pop()

            curr_str.append(')')
            backtracking(close_c + 1, open_c)
            curr_str.pop()
        
        backtracking(0, 0)
        return res