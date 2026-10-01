class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        
        def can_form(mid):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p
        
        left, right = 0, nums[-1] - nums[0]
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if can_form(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans