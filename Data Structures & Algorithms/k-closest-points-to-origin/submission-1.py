class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(point[0]**2 + point[1]**2), point) for point in points]
        heapq.heapify(distances)
        
        res = []
        while distances and k:
            k -= 1
            res.append(heapq.heappop(distances)[-1])
        
        return res