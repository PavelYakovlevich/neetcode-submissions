# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def quickSortCore(l: int, r: int):
            if r - l + 1 <= 1:
                return pairs
            
            pivot = pairs[r]
            ins = l

            for i in range(l, r):
                if pairs[i].key < pivot.key:
                    pairs[ins], pairs[i] = pairs[i], pairs[ins]
                    ins += 1
            
            pairs[ins], pairs[r] = pivot, pairs[ins]

            quickSortCore(l, ins - 1)
            quickSortCore(ins + 1, r)

            return pairs
        
        return quickSortCore(0, len(pairs) - 1)