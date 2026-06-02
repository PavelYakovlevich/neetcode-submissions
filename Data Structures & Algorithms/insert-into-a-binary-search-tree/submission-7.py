# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        p = root

        while True:
            if val <= p.val:
                if not p.left:
                    p.left = TreeNode(val)
                    return root
                p = p.left
            else:
                if not p.right:
                    p.right = TreeNode(val)
                    return root
                p = p.right