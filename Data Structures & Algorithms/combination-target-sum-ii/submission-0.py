class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        curr_candidates = []
        res = []
        def backtracking(i: int, curr_sum: int):
            if curr_sum == target:
                res.append(curr_candidates.copy())
                return

            if i >= len(candidates) or curr_sum > target:
                return
            
            curr_candidates.append(candidates[i])
            backtracking(i + 1, curr_sum + candidates[i])
            curr_candidates.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtracking(i + 1, curr_sum)

        backtracking(0, 0)
        
        return res