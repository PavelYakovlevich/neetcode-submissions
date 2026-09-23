class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append([v, price])
        
        q = deque([(0, src, 0)])
        while q:
            price, node, stops = q.popleft()
            if stops > k:
                continue
            
            for neightbor, neightbor_price in adj[node]:
                next_cost = price + neightbor_price
                if next_cost < prices[neightbor]:
                    prices[neightbor] = next_cost
                    q.append((next_cost, neightbor, stops + 1))
        
        return prices[dst] if prices[dst] != float('inf') else -1