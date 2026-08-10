# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        i = k

        while i <= len(lst):
            lst[i - k: i] = lst[i - k: i][::-1]
            i += k
        
        curr = mock = ListNode()

        for node in lst:
            curr.next = ListNode(node)
            curr = curr.next
        
        return mock.next

        
        
    