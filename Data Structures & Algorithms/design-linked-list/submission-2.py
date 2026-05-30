class MyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0;

    def get(self, index: int) -> int:
        if index >= self._size or index < 0:
            return -1

        curr = self._head
        for i in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        if self._size == 0:
            self._head = Node(val)
        else:
            self._head.prev = Node(val);
            self._head.prev.next = self._head
            self._head = self._head.prev

        self._size += 1

    def addAtTail(self, val: int) -> None:
        curr = self._head

        while curr.next is not None:
            curr = curr.next

        curr.next = Node(val)

        curr.next.prev = curr

        self._size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self._size:
            return

        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self._size:
            self.addAtTail(val)
            return
        
        curr = self._head
        for i in range(index):
            curr = curr.next
        
        newNode = Node(val)

        curr.prev.next = newNode
        
        newNode.prev = curr.prev
        newNode.next = curr

        curr.prev = newNode

        self._size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._size:
            return
        if index == 0:
            self._head = self._head.next if self._size > 1 else None
            self._size -= 1
            return

        curr = self._head
        for i in range(index):
            curr = curr.next
        
        self._size -= 1
        if curr.next is not None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        else:
            curr.prev.next = None
        
class Node:
    def __init__(self, value: int):
        self.next = None
        self.prev = None
        self.val = value

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)