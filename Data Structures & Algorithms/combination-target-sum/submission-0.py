class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        curr_combination = []

        def backtracking(index: int, curr_sum: int):
            if curr_sum == target:
                combinations.append(list(curr_combination))
                return
            if curr_sum > target or index == len(nums):
                return
            
            curr_combination.append(nums[index])
            backtracking(index, curr_sum + nums[index])
            
            curr_combination.pop()
            backtracking(index + 1, curr_sum)

        backtracking(0, 0)

        return combinations