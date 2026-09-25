class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        baskets_cap = res = L = 0
        for fruit in fruits:
            baskets_cap += 1

            if fruit not in window:
                window[fruit] = 0
            window[fruit] += 1

            while len(window) > 2:
                window[fruits[L]] -= 1
                baskets_cap -= 1
                if not window[fruits[L]]:
                    del window[fruits[L]]
                L += 1
            
            res = max(res, baskets_cap)
        return res
