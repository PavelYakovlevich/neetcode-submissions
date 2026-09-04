"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def bfs(node: 'Node'):
            if not node:
                return
            
            for child in node.children:
                bfs(child)
            
            res.append(node.val)
        
        bfs(root)

        return res