class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            pivot = L + (R - L) // 2

            if target == nums[pivot]:
                return pivot
            
            if target < nums[pivot]:
                R = pivot - 1
            else:
                L = pivot + 1
        
        return L