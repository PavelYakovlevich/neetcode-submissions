class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)

        for string in arr:
            if cnt[string] == 1:
                k -= 1
                if k == 0:
                    return string
        
        return ''