class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i, edge in enumerate(edges):
            src, dst = edge
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))
        
        visit = set()
        max_heap = [(-1.0, start_node)]
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            
            if node in visit:
                continue
            
            visit.add(node)

            if node == end_node:
                return -prob

            for dst, dst_prob in adj[node]:
                if dst in visit:
                    continue
                
                heapq.heappush(max_heap, (prob * dst_prob, dst))
        
        return 0