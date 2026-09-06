# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        res = curr_sum = 0

        while root or stack:
            if root:
                curr_sum = curr_sum * 10 + root.val
                stack.append((root, curr_sum))
                root = root.left 
            else:
                root, curr_sum = stack.pop()
                if not root.left and not root.right:
                    res += curr_sum
                
                root = root.right
        
        return res
