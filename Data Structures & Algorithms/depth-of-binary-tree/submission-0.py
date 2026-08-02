# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        max_depth = 0
        curr_depth = 1

        while root or stack:
            if not root:
                root, curr_depth = stack.pop()
            else:
                stack.append((root.right, curr_depth + 1))
                max_depth = max(max_depth, curr_depth)
                root = root.left
                curr_depth += 1
        
        return max_depth