class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        
        heap = []
        for ch, count in cnt.items():
            heapq.heappush(heap, [-count, ch])
        
        res = []
        while heap:
            neg_count, char = heapq.heappop(heap) 
            res.extend([char] * (-neg_count))
        
        return ''.join(res)