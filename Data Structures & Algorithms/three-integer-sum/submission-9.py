class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                triplet = [nums[i], nums[l], nums[r]]
                triplet_sum = sum(triplet)
                if triplet_sum == 0:
                    res.append(triplet)
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif triplet_sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res