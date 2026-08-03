# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next

        lst.pop(len(lst) - n)

        head = ListNode()
        curr = head
        for i in range(len(lst)):
            curr.next = ListNode(lst[i])
            curr = curr.next

        return head.next