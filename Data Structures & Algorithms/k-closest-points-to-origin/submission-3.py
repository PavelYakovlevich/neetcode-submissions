class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        calc_distance = lambda p: p[0] ** 2 + p[1] ** 2

        def partion(l, r):
            pivot_index = r
            pivot_distance = calc_distance(points[pivot_index])
            i = l
            for j in range(l, pivot_index):
                if pivot_distance >= calc_distance(points[j]):
                    points[i], points[j] = points[j], points[i]
                    i += 1
            
            points[i], points[pivot_index] = points[pivot_index], points[i]
            return i
        
        l, r = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partion(l, r)
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
            
        return points[:k]