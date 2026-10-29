# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        
        head = dummy = ListNode()
        curr = head
        for node in stack:
            curr.next = ListNode(node)
            curr = curr.next
        return dummy.next
