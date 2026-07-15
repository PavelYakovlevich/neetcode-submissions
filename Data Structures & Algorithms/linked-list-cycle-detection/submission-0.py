# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()

        def dfs(curr):
            if not curr:
                return False
            
            if curr in visit:
                return True
            
            visit.add(curr)
            
            return dfs(curr.next)

        return dfs(head)