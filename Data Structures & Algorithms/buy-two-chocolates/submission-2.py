class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        minimum_cost = prices[0] + prices[1]

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                minimum_cost = min(minimum_cost, prices[i] + prices[j])
        
        return money - minimum_cost if money >= minimum_cost else money