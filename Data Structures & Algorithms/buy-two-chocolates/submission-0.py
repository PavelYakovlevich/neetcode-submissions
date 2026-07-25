class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        leftovers = money - (prices[0] + prices[1])
        return leftovers if leftovers >= 0 else money