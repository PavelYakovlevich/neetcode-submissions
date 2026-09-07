class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort()

        merged = [intervals[0]]
        next_intv_idx = 1

        while next_intv_idx < len(intervals):
            next_intv = intervals[next_intv_idx]
            last_intv = merged[-1]

            can_be_merged = next_intv[0] <= last_intv[1]
            
            if can_be_merged:
                merged[-1][0], merged[-1][-1] = min(last_intv[0], next_intv[0]), max(last_intv[-1], next_intv[-1])
            else:
                merged.append(next_intv)
                
            next_intv_idx += 1
        
        return merged