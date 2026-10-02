class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []
        for string in strs:
            cnt = Counter(string)
            counts.append((cnt['0'], cnt['1']))
        
        memo = {}
        def backtracking(i, zeros_left, ones_left):
            if i >= len(strs):
                return 0
            if (i, zeros_left, ones_left) in memo:
                return memo[(i, zeros_left, ones_left)]
            
            res = backtracking(i + 1, zeros_left, ones_left)
            
            z, o = counts[i]
            if zeros_left >= z and ones_left >= o:
                res = max(res, 1 + backtracking(i + 1, zeros_left - z, ones_left - o))
            
            memo[(i, zeros_left, ones_left)] = res
            return res
        
        return backtracking(0, m, n)