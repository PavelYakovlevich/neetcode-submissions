class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            curr_permutations = []
            for p in permutations:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, n)
                    curr_permutations.append(copy)
            
            permutations = curr_permutations
        
        return permutations