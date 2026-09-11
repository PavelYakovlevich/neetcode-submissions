class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        curr = []
        res = []

        def backtracking(digit_index):
            if len(curr) == len(digits):
                res.append(''.join(curr))
                return

            for char in digit_map[digits[digit_index]]:
                curr.append(char)
                backtracking(digit_index + 1)
                curr.pop()

        backtracking(0)
        return res