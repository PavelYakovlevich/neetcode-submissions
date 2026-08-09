# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        curr = root

        while curr or stack:
            if curr:
                curr.left, curr.right = curr.right, curr.left
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        return root

                