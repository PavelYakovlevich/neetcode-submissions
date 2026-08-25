class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        local_max = float('-inf')
        res = 0
        while root or stack:
            if root:
                if root.val >= local_max:
                    res += 1
                local_max = max(local_max, root.val)
                stack.append((root, local_max))
                root = root.left
            else:
                root, local_max = stack.pop()
                root = root.right

        return res