class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        
        for i in range(len(self.prices) - 1, -1, -1):
            if price < self.prices[i]:
                return len(self.prices) - i - 1
        return len(self.prices)
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)