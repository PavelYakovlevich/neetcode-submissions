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
        q = deque([root])
        while q:
            res.append([])

            for i in range(len(q)):
                node = q.popleft()
                res[-1].append(node.val)

                for child in [node.left, node.right]:
                    if child:
                        q.append(child)
            
        return res
