"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res, stack = [], []
        processed_children_count = 0
        while root or stack:
            if root:
                are_all_children_processed = not root.children or processed_children_count == len(root.children)

                if are_all_children_processed:
                    res.append(root.val)
                    root = None
                else:
                    stack.append((root, processed_children_count + 1))
                    root = root.children[processed_children_count]
                    processed_children_count = 0
            else:
                root, processed_children_count = stack.pop()

        return res

        # res = []

        # def dfs(node):
        #     if not node:
        #         return
            
        #     for child in node.children:
        #         dfs(child)

        #     res.append(node.val)

        # dfs(root)
        
        # return res