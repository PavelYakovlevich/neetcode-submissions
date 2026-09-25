class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        res = L = 0
        for R, fruit in enumerate(fruits):
            if fruit not in window:
                window[fruit] = 0
            window[fruit] += 1

            while len(window) > 2:
                window[fruits[L]] -= 1
                if not window[fruits[L]]:
                    del window[fruits[L]]
                L += 1
            
            res = max(res, R - L + 1)
        return res
