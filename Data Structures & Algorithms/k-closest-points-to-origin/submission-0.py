class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            heapq.heappush(heap, (math.sqrt(point[0]**2 + point[1]**2), point))
        
        res = []
        while heap and k:
            k -= 1
            res.append(heapq.heappop(heap)[-1])
        
        return res