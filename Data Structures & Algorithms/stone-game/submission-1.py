class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dfs(l, r):
            if (l, r) in cache:
                return cache[(l, r)]
            if l > r:
                return 0
            
            max_score = 0
            for pile, l_new, r_new in [[piles[l], l + 1, r], [piles[r], l, r - 1]]:
                alice_step_score = 0 if (r - l + 1) & 1 else pile
                score = alice_step_score + dfs(l_new, r_new)
                cache[(l_new, r_new)] = score
                max_score = max(max_score, score)
            return max_score

        alice_score = dfs(0, len(piles) - 1)
        scores = sum(piles)

        return scores // 2 < alice_score