class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_buy_price, profit = prices[0], 0

        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                last_buy_price = prices[i]
            elif prices[i] > prices[i - 1]:
                profit += prices[i] - last_buy_price
                last_buy_price = prices[i]

        return profit
