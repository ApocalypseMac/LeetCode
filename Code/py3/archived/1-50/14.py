class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        result = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(result) and j < len(strs[i]):
                if result[j] == strs[i][j]:
                    j += 1
                else:
                    break
            if j == 0:
                return ""
            else:
                result = result[0:j]
        return result
        