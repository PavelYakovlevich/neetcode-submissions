class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = set()

        perms = [[]]

        for n in nums:
            curr_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    c = p.copy()
                    c.insert(i, n)

                    p_tuple = tuple(c)
                    if p_tuple not in seen:
                        seen.add(p_tuple)
                        curr_perms.append(c)
            
            perms = curr_perms

        return perms