class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1:
            return [arr[0]]

        heap = []
        for num in arr:
            heapq.heappush(heap, [abs(num - x), num])
        
        res = []
        while k > 0:
            _, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        res.sort()

        return res
        