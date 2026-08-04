class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        insert_pos = 0
        for num2 in arr2:
            for i in range(insert_pos, len(arr1)):
                if num2 == arr1[i]:
                    arr1[i], arr1[insert_pos] = arr1[insert_pos], arr1[i]
                    insert_pos += 1
        
        arr1[insert_pos:len(arr1)] = sorted(arr1[insert_pos:len(arr1)])

        return arr1
            

        
        