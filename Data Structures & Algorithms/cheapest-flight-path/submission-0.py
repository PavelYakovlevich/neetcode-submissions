class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for frm, to, price in flights:
            adj[frm].append([to, price])

        stops = {}
        heap = [[0, 0, src]]
        while heap:
            price, stop, src_node = heapq.heappop(heap)
            if src_node in stops and stops[src_node] <= stop:
                continue

            stops[src_node] = stop

            if dst == src_node:
                return price
            
            if stop <= k:
                for to, to_price in adj[src_node]:
                    heapq.heappush(heap, [price + to_price, stop + 1, to])
        
        return -1