# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverse_list(head)
        
        mock = ListNode(next=head)
        curr = prev = mock
        while n:
            n -= 1
            prev = curr
            curr = curr.next
            
        prev.next = curr.next

        return self.reverse_list(mock.next)

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
