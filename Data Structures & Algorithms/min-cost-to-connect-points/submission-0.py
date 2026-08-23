class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        manhattan_dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        for i in range(len(points)):
            src_x, src_y = points[i]
            for j in range(i + 1, len(points)):
                dst_x, dst_y = points[j]
                
                dist = manhattan_dist(points[i], points[j])
                adj[(src_x, src_y)].append((dst_x, dst_y, dist))
                adj[(dst_x, dst_y)].append((src_x, src_y, dist))

        min_heap = []
        for x, y, dist in adj[(points[0][0], points[0][1])]:
            heapq.heappush(min_heap, (dist, x, y))
        
        seen = set([(points[0][0], points[0][1])])
        res = 0
        while min_heap:
            src_dist, src_x, src_y = heapq.heappop(min_heap)
            if (src_x, src_y) in seen:
                continue
            
            seen.add((src_x, src_y))
            res += src_dist

            for dst_x, dst_y, dst_dist in adj[(src_x, src_y)]:
                if (dst_x, dst_y) in seen:
                    continue

                heapq.heappush(min_heap, (dst_dist, dst_x, dst_y))
        
        return res
