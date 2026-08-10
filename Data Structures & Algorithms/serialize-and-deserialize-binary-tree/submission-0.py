class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()

            res.append(str(node.val if node else None))

            if not node:
                continue

            queue.append(node.left)
            queue.append(node.right)
        return '|'.join(res)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        nodes = data.split('|')

        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()
            
            if i < len(nodes) and nodes[i] != 'None':
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1

            if i < len(nodes) and nodes[i] != 'None':
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1

        return root