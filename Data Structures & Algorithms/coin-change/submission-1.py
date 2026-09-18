class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(left: int) -> int:
            if left == 0:
                return 0
            if left in memo:
                return memo[left]

            res = float('inf')
            for coin in coins:
                if left - coin >= 0:
                    res = min(res, 1 + dfs(left - coin))
            
            memo[left] = res
            return res

        res = dfs(amount)
        
        return res if res != float('inf') else -1