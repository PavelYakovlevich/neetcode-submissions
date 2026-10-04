class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        p1 = p2 = 0
        while p1 < len(slots1) and p2 < len(slots2):
            start1, end1 = slots1[p1]
            start2, end2 = slots2[p2]
            
            overlap_start = max(start1, start2)
            overlap_end = min(end1, end2)
            
            if overlap_end - overlap_start >= duration:
                return [overlap_start, overlap_start + duration]
            
            if end1 < end2:
                p1 += 1
            else:
                p2 += 1

        return []