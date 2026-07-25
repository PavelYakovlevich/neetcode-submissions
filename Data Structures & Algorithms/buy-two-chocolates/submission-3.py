class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_chocho = min(prices[0], prices[1])
        max_chocho = max(prices[0], prices[1])

        for i in range(2, len(prices)):
            if prices[i] < max_chocho:
                if prices[i] > min_chocho:
                    max_chocho = prices[i]
                else:
                    max_chocho = min_chocho
                    min_chocho = prices[i]
        
        diff = money - (min_chocho + max_chocho)

        return diff if diff >= 0 else money