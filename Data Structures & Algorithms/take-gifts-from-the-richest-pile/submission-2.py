import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        
        for i in range(k):
            pile = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, math.floor(math.sqrt(pile)))
        
        return sum(gifts)
