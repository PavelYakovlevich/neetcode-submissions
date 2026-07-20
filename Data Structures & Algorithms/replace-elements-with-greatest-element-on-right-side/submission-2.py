class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_el = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_el
            max_el = max(max_el, temp)
        
        return arr