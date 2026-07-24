class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1 in nums1:
            i = 0
            while num1 != nums2[i]:
                i += 1
            
            greater_num = -1
            for j in range(i + 1, len(nums2)):
                if nums2[j] > num1:
                    greater_num = nums2[j]
                    break
            
            res.append(greater_num)
        
        return res

