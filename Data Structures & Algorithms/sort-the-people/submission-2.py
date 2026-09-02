class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = sorted(zip(heights, names), key=lambda x: x[0], reverse=True)

        return [name for h, name in combined]