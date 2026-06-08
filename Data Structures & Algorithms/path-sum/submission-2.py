# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return bool(root) and self.has_path_sum(root, 0, targetSum)
        
    def has_path_sum(self, root, acc, target_sum):
            if not root.left and not root.right:
                return (acc + root.val) == target_sum
            
            if root.left and self.has_path_sum(root.left, acc + root.val, target_sum):
                return True
                        
            if root.right and self.has_path_sum(root.right, acc + root.val, target_sum):
                return True
            
            return False