# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def dfs(node):
            nonlocal max_sum
            
            if not node:
                return 0
            
            l_max_sum, r_max_sum = max(0, dfs(node.left)), max(0, dfs(node.right))
           
            max_sum = max(max_sum, node.val + l_max_sum + r_max_sum)

            return node.val + max(l_max_sum, r_max_sum)

        dfs(root)
        return max_sum