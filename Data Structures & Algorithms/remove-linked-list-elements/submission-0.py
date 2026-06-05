# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        p = head

        while p:
            if p.val == val:
                if not prev:
                    head = p.next
                elif not p.next:
                    prev.next = None
                else:
                    prev.next = p.next
            else:
                prev = p

            p = p.next
        
        return head

