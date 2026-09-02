class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)

        for string in arr:
            if cnt[string] == 1:
                if k == 1:
                    return string
                else:
                    k -= 1
        
        return ''