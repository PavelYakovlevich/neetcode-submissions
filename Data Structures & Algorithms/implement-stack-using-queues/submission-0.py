import queue

class MyStack:
    def __init__(self):
       self._q = None

    def push(self, x: int) -> None:
        self._q = deque([x, self._q])

    def pop(self) -> int:
        top = self._q.popleft()
        self._q = self._q.popleft()
        return top

    def top(self) -> int:
        return self._q[0]

    def empty(self) -> bool:
        return not self._q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()