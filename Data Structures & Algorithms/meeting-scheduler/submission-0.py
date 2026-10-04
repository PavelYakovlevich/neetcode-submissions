class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        p1 = p2 = 0
        while p1 < len(slots1) and p2 < len(slots2):
            slot1, slot2 = slots1[p1], slots2[p2]
            if max(slot1[0], slot2[0]) <= min(slot1[-1], slot2[-1]):
                start = max(slot1[0], slot2[0])
                end = start + duration
                if end <= min(slot1[-1], slot2[-1]):
                    return [start, end]
            if slot1[-1] < slot2[-1]:
                p1 += 1
            else:
                p2 += 1
        return []