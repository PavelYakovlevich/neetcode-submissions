class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        order = []
        visit, path = set(), set()

        def dfs(node: int) -> bool:
            if node in path:
                return False

            if node in visit:
                return True
            
            path.add(node)

            for next_course in adj[node]:
                if not dfs(next_course):
                    return False
            
            path.remove(node)
            visit.add(node)
            order.append(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return order