class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices_count = 0

    def next(self, price: int) -> int:
        self.prices_count += 1

        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()

        span = self.prices_count - (self.stack[-1][1] if self.stack else 0)
        self.stack.append([price, self.prices_count])

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)