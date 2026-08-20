class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(i, combination):
            if len(combination) == k:
                res.append(combination.copy())
                return

            if i > n:
                return 

            combination.append(i)
            backtracking(i + 1, combination)
            combination.pop()
            
            backtracking(i + 1, combination)

        backtracking(1, [])

        return res