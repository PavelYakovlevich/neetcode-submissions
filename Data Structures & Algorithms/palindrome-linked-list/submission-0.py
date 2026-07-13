# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        def dfs(curr):
            if not curr:
                return
            
            dfs(curr.next)
            lst.append(curr.val)


        dfs(head)
        i = 0
        while head:
            if lst[i] != head.val:
                return False
            i += 1
            head = head.next
        
        return True

        