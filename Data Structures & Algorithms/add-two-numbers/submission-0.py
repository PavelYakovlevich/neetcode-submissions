# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        curr = res
        remainder = 0
        while l1 or l2 or remainder:
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val
            calc =  l1_val + l2_val + remainder
            curr.next = ListNode(calc % 10)
            remainder = calc // 10
            curr = curr.next
            if l2: 
                l2 = l2.next
            if l1: 
                l1 = l1.next

        return res.next