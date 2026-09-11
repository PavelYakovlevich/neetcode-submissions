"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = {}
        
        def dfs(curr):
            if not curr:
                return None
                
            if curr in visit:
                return visit[curr]
            
            curr_copy = Node(curr.val)
            visit[curr] = curr_copy

            for neighbor in curr.neighbors:
                curr_copy.neighbors.append(dfs(neighbor))
            
            return curr_copy
        
        return dfs(node)