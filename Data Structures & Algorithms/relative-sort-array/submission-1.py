class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_num1 = max(arr1)
        counter = [0] * (max_num1 + 1)

        for num1 in arr1:
            counter[num1] += 1
        
        res = []
        for num2 in arr2:
            res += [num2] * counter[num2]
            counter[num2] = 0
        
        for i, count in enumerate(counter):
            if count:
                res += [i] * count
        
        return res
        

        
        