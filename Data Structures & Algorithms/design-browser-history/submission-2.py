class BrowserHistory:
    def __init__(self, homepage: str):
        self._head = Node('')
        self._tail = Node('')

        base = Node(homepage, self._tail, self._head)
        self._head.next = base
        self._tail.prev = base
        self._current = base

    def visit(self, url: str) -> None:
        newNode = Node(url, self._tail, self._current)

        self._current.next = newNode
        newNode.prev = self._current

        self._tail.prev = newNode

        self._current = newNode

    def back(self, steps: int) -> str:
        while steps > 0 and self._current != self._head.next:
            self._current = self._current.prev
            steps -= 1
        
        return self._current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self._current is not self._tail.prev:
            self._current = self._current.next
            steps -= 1

        return self._current.val

class Node:
    def __init__(self, val: str, next: Node = None, prev: Node = None):
        self.val = val
        self.next = next
        self.prev = prev