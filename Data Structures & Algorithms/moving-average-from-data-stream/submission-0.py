class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.buffer = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.buffer) == self.size:
            self.sum -= self.buffer[0]
            self.buffer.popleft()
        
        self.sum += val
        self.buffer.append(val)
        return self.sum / len(self.buffer)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
