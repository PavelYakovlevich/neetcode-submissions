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
        prev = None
        while p:
            prev = p

            if p.val >= val:
                p = p.left
            else:
                p = p.right
        
        if prev and val <= prev.val:
            prev.left = TreeNode(val)
        elif prev and val > prev.val:
            prev.right = TreeNode(val)

        return root