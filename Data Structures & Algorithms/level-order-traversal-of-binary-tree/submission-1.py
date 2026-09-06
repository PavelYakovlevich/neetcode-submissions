# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res = []
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if level >= len(res):
                res.append([])
            
            res[level].append(node.val)

            for child in [node.left, node.right]:
                if child:
                    q.append((child, level + 1))
            
        return res
