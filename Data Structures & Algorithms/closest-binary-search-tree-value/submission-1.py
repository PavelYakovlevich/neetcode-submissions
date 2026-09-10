# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_val = root.val
        while root:
            diff = root.val - target
            if abs(diff) < abs(closest_val - target):
                closest_val = root.val
            root = root.left if diff > 0 else root.right

        return closest_val
