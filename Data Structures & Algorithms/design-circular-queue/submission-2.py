class MyCircularQueue:

    def __init__(self, k: int):
        self.count = 0
        self.front = 0
        self.rear = -1
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = value
        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.queue[self.front] = 0
        self.front = (self.front + 1) % len(self.queue)
        self.count -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return not self.count

    def isFull(self) -> bool:
        return self.count == len(self.queue)