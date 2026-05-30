class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        smallest_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] - smallest_price > max_profit:
                max_profit = prices[i] - smallest_price

            if prices[i] < smallest_price:
                smallest_price = prices[i]

        return max_profit