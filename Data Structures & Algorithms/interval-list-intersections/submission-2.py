class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            start_a, end_a = firstList[i]
            start_b, end_b = secondList[j]

            start, end = max(start_a, start_b), min(end_a, end_b)
            if start <= end:
                res.append([start, end])
            
            if end_a < end_b:
                i += 1
            else:
                j += 1
        return res
