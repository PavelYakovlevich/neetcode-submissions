"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_map = {}
        
        deep_copy = Node(-1)

        curr, curr_copy = head, deep_copy
        while curr:
            curr_copy.next = Node(curr.val)
            curr_copy = curr_copy.next

            nodes_map[curr] = curr_copy
            
            curr = curr.next
        
        curr, curr_copy = head, deep_copy.next
        while curr:
            if curr.random:
                curr_copy.random = nodes_map[curr.random]
            
            curr, curr_copy = curr.next, curr_copy.next

        return deep_copy.next