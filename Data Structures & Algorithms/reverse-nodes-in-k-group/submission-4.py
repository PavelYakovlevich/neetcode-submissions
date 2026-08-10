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

        for i in range(k, len(lst) + 1, k):
            l, r = i - k, i - 1

            while l < r:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
        
        curr = mock = ListNode()

        for node in lst:
            curr.next = ListNode(node)
            curr = curr.next
        
        return mock.next

        
        
    