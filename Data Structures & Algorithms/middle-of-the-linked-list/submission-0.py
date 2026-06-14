class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.length = 0

        def traverse(node: Optional[ListNode], index: int):
            if not node:
                return None
            
            self.length += 1
            
            res = traverse(node.next, index + 1)

            if self.length // 2 == index:
                return node
            return res

        return traverse(head, 0)