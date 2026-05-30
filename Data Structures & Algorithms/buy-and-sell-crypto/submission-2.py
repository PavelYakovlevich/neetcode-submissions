class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices) - 1, 0, -1):
            for j in range(i):
                if prices[i] - prices[j] > max_profit:
                    max_profit = prices[i] - prices[j]

        return max_profit 