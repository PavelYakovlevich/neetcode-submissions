class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                candidate = [nums[i], nums[l], nums[r]]
                tree_sum = sum(candidate) 
                
                if tree_sum > 0:
                    r -= 1
                elif tree_sum < 0:
                    l += 1
                else:
                    res.append(candidate)

                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res