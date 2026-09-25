class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        normalized = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= normalized[-1][1]:
                normalized.append(intervals[i])

        return len(intervals) - len(normalized)