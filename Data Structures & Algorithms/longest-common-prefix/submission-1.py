class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''

        for i in range(len(strs[0])):
            common_prefix = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    common_prefix = False
                    break
                common_prefix = common_prefix and strs[0][i] == strs[j][i]

            if common_prefix:
                prefix += strs[0][i]
            else:
                break

        return prefix