class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        p1 = p2 = 0
        while p1 < len(slots1) and p2 < len(slots2):
            slot1, slot2 = slots1[p1], slots2[p2]
            start1, end1 = slot1
            start2, end2 = slot2
            if max(start1, start2) <= min(end1, end2):
                candidate_start = max(start1, start2)
                candidate_end = candidate_start + duration
                if candidate_end <= min(end1, end2):
                    return [candidate_start, candidate_end]
            if end1 < end2:
                p1 += 1
            else:
                p2 += 1
        return []