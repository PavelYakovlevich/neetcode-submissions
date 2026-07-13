# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        acc = 0
        i = 0
        while i < length // 2:
            acc += head.val
            i += 1
            head = head.next

        if length & 1:
            head = head.next 

        while head:
            acc -= head.val
            head = head.next
        
        return not acc


        