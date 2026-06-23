class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = [0] * 501

        for num in arr:
            cnt[num] += 1
        
        for i in range(len(cnt) - 1, 0, -1):
            if cnt[i] == i:
                return i
        
        return -1

