# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        height = 1
        while root or stack:
            if root:    
                if height > len(res):
                    res.append(root.val)
                stack.append((height, root))
                height += 1
                root = root.right
            else:
                height, root = stack.pop()
                height += 1
                root = root.left
        
        return res