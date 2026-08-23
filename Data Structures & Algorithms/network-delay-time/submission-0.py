class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dest, weight in times:
            adj[src].append((dest, weight))
        
        mins = {}
        min_heap = [(0, k)]
        res = 0
        while min_heap:
            weight, vertice = heapq.heappop(min_heap)
            if vertice in mins:
                continue
            
            mins[vertice] = weight
            res = max(res, weight)

            for dest, dest_weight in adj[vertice]:
                if dest in mins:
                    continue
                
                heapq.heappush(min_heap, (weight + dest_weight, dest))
        
        return -1 if n != len(mins) else res
