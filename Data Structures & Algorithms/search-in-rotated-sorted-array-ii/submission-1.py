class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i = 0

        while i < len(nums) - 1 and nums[i] <= nums[i+1]:
            i += 1
        
        L, R = 0, len(nums) - 1

        if target >= nums[0]:
            R = i
        else:
            L = i + 1
        
        while L <= R:
            m = L + (R - L) // 2
            
            if nums[m] == target:
                return True
            if target > nums[m]:
                L = m + 1
            else:
                R = m - 1
        
        return False