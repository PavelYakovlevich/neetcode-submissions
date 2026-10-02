class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            building_height = heights[i]
            if building_height > max_height:
                res.append(i)
                max_height = building_height
        
        return res[::-1]